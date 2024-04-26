from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
import os
import uuid
from werkzeug.utils import secure_filename


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
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        date_of_birth = request.form['date_of_birth']
        gender = request.form['gender']
        contact_number = request.form['contact_number']
        email = request.form['email']
        address = request.form['address']
        program = request.form['program']
        gpa = request.form['gpa']
        accommodation = request.form.get('accommodation', False)
        academic_transcripts = request.files.get('academic_transcripts')
        personal_doc = request.files.get('personal_doc')

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
            students.insert_one({'firstname': firstname, 'lastname': lastname, 'date_of_birth': date_of_birth, 'gender': gender, 'contact_number':contact_number, 'email':email, 'address':address, 'program':program, 'gpa': gpa, 'accommodation':accommodation, 'personal_doc_unique_filename': personal_doc_unique_filename, 'academic_transcripts_unique_filename': academic_transcripts_unique_filename})
            return redirect(url_for('index'))
            
    all_students = students.find()
    return render_template('index.html', students=all_students)

if __name__ == '__main__':
    app.run(debug=True)