from flask import Flask, render_template, request, url_for, redirect, send_from_directory, session, jsonify
from pymongo import MongoClient
import os
import uuid
from werkzeug.utils import secure_filename
from operator import itemgetter
from bson import ObjectId

app = Flask(__name__)
client = MongoClient('localhost', 27017)

# Mongo database
db = client.students_database
students = db.students
files_collection = db.files

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def create_upload_folder():
    upload_path = app.config['UPLOAD_FOLDER']
    if not os.path.exists(upload_path):
        os.makedirs(upload_path)


def create_files_collection():
    if 'files' not in db.list_collection_names():
        db.create_collection('files')


@app.route("/", methods=["GET", "POST"])
def index():
    create_upload_folder()
    create_files_collection()

    if request.method == "POST":
        # Get form data
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        date_of_birth = request.form.get('date_of_birth')
        gender = request.form.get('gender')
        contact_number = request.form.get('contact_number')
        email = request.form.get('email')
        address = request.form.get('address')
        program = request.form.get('program')
        gpa = request.form.get('gpa')
        accommodation = request.form.get('accommodation') == 'True'  # Check if checkbox is checked
        academic_transcripts = request.files.get('academic_transcripts')
        personal_doc = request.files.get('personal_doc')

        # Validate required fields
        if not firstname or not lastname or not email:
            return "Please provide required information."

        # Handling uploads
        files = []

        if academic_transcripts:
            academic_transcripts_filename = secure_filename(academic_transcripts.filename)
            academic_transcripts_unique_filename = str(uuid.uuid4()) + os.path.splitext(academic_transcripts_filename)[1]
            academic_transcripts.save(os.path.join(app.config['UPLOAD_FOLDER'], academic_transcripts_unique_filename))
            academic_transcripts_url = f'{request.host_url}{UPLOAD_FOLDER}/{academic_transcripts_unique_filename}'
            files.append({'file_name': academic_transcripts_filename, 'file_url': academic_transcripts_url})

        if personal_doc:
            personal_doc_filename = secure_filename(personal_doc.filename)
            personal_doc_unique_filename = str(uuid.uuid4()) + os.path.splitext(personal_doc_filename)[1]
            personal_doc.save(os.path.join(app.config['UPLOAD_FOLDER'], personal_doc_unique_filename))
            personal_doc_url = f'{request.host_url}{UPLOAD_FOLDER}/{personal_doc_unique_filename}'
            files.append({'file_name': personal_doc_filename, 'file_url': personal_doc_url})

        if files:
            db.files.insert_many(files)

        # Insert student data into the database
        student_data = {
            'firstname': firstname,
            'lastname': lastname,
            'date_of_birth': date_of_birth,
            'gender': gender,
            'contact_number': contact_number,
            'email': email,
            'address': address,
            'program': program,
            'gpa': gpa,
            'accommodation': accommodation,
            'personal_doc_unique_filename': personal_doc_unique_filename,
            'personal_doc_filename': personal_doc_filename,
            'academic_transcripts_unique_filename': academic_transcripts_unique_filename,
            'academic_transcripts_filename': academic_transcripts_filename
        }
        students.insert_one(student_data)

        return redirect(url_for('index'))

    all_students = students.find({})
    return render_template('index.html', students=all_students)



@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)


secret_key = str(uuid.uuid4())
app.secret_key = secret_key


@app.route("/portal", methods=["GET"])
def render_portal():
    all_students = students.find({})
    
    # Convert cursor object to a list of dictionaries and convert ObjectId to string
    all_students = list(all_students)
    all_students = [{**student, "_id": str(student["_id"])} for student in all_students]

    return render_template("portal.html", students=all_students)

@app.route("/sort", methods=["POST"])
def sort_data():
    all_students = students.find({})
    sort_by = request.json.get("sortBy")
    sort_order = request.json.get("sortOrder")

    # Store the sorting parameters in session variables
    session["sort_by"] = sort_by
    session["sort_order"] = sort_order

    if sort_by and sort_order:
        sort_by = sort_by or "firstname"
        # Sort the students list based on the sort_by key
        all_students = sorted(all_students, key=lambda x: x[sort_by])

        if sort_order == "descending":
            # Reverse the list if the sort_order is "descending"
            all_students = list(reversed(all_students))

    # Convert cursor object to a list of dictionaries and convert ObjectId to string
    all_students = list(all_students)
    all_students = [{**student, "_id": str(student["_id"])} for student in all_students]

    return jsonify(all_students)
if __name__ == '__main__':
    app.run(debug=True)