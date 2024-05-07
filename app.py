from flask import Flask, render_template, request, url_for, redirect, send_from_directory, session, jsonify
from pymongo import MongoClient
import os
import uuid
from bson import ObjectId
from werkzeug.utils import secure_filename
from sortingalgorithms import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort,heap_sort
from searchingalgorithms import linear_search, binary_search ,exponential_search,hash_table_search, interpolation_search, ternary_search
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)
client = MongoClient('localhost', 27017)

# Mongo database conn
db = client.students_database
students = db.students
files_collection = db.files

secret_key = str(uuid.uuid4())
app.secret_key = secret_key

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['STATIC_FOLDER'] = 'static'


def create_upload_folder():
    upload_path = app.config['UPLOAD_FOLDER']
    if not os.path.exists(upload_path):
        os.makedirs(upload_path)


def create_files_collection():
    if 'files' not in db.list_collection_names():
        db.create_collection('files')


@app.route("/", methods=["GET", "POST"])
def index():
    alert_message = None
    create_upload_folder()
    create_files_collection()

    if request.method == "POST":
        alert_message = "Data submited successfully"
        
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
            'firstname': firstname.title(),
            'lastname': lastname.title(),
            'date_of_birth': date_of_birth,
            'gender': gender.title(),
            'contact_number': contact_number,
            'email': email,
            'address': address.title(),
            'program': program.title(),
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
    return render_template('index.html', students=all_students, alert_message=alert_message)



@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)


@app.route("/portal", methods=["GET"])
def render_portal():
    all_students = students.find({})
    
    # Convert cursor object to a list of dictionaries and convert ObjectId to string
    all_students = list(all_students)
    all_students = [{**student, "_id": str(student["_id"])} for student in all_students]

    return render_template("portal.html", students=all_students)


@app.route("/sort", methods=["POST"])
def sort_data():
    all_students = list(students.find({}))
    sort_by = request.json.get("sortBy")
    sort_order = request.json.get("sortOrder")
    sort_algorithm = request.json.get("sortAlgorithm")
    
    sort_by = 'firstname' if sort_by == "" else sort_by
    sort_algorithm = 'bubble_sort' if sort_algorithm == "" else sort_algorithm

    # Store the sorting parameters in session variables
    session["sort_by"] = sort_by
    session["sort_order"] = sort_order
    session["sort_algorithm"] = sort_algorithm
    

    if sort_by and sort_order and sort_algorithm:  
      
        if sort_algorithm == 'bubble_sort':
            all_students = bubble_sort(all_students, sort_by)
        elif sort_algorithm == 'selection_sort':
            all_students = selection_sort(all_students, sort_by)
        elif sort_algorithm == 'insertion_sort':
            all_students = insertion_sort(all_students, sort_by)
        elif sort_algorithm == 'quick_sort':
            all_students = quick_sort(all_students, sort_by)
        elif sort_algorithm == 'merge_sort':
            all_students = merge_sort(all_students, sort_by)
        elif sort_algorithm == 'heap_sort':
            all_students = heap_sort(all_students, sort_by)
        else:
            return jsonify(error='Invalid sort algorithm')

        

        if sort_order == "descending":
            all_students = all_students[::-1]


    all_students = [{**student, "_id": str(student["_id"])} for student in all_students]

    return jsonify(all_students)


@app.route("/search", methods=["POST"])
def search_data():
    all_students = list(students.find({}))
    search_term = request.json.get("searchTerm")
    search_algorithm = request.json.get("searchAlgorithm")

    matching_students = []  # Initialize matching_students as an empty list

    if search_algorithm == 'binary_search':
        matching_students = binary_search(all_students, search_term)
    elif search_algorithm == 'linear_search':
        matching_students = linear_search(all_students, search_term)
    elif search_algorithm == 'hash_table_search':
        matching_students = hash_table_search(all_students, search_term)
    elif search_algorithm == 'interpolation_search':
        matching_students = interpolation_search(all_students, search_term)
    elif search_algorithm == 'ternary_search':
        matching_students = ternary_search(all_students, search_term)
    elif search_algorithm == 'exponential_search':
        matching_students = exponential_search(all_students, search_term)

   
    if not isinstance(matching_students, list):
        matching_students = []

  
    matching_students = [{**student, "_id": str(student["_id"])} if isinstance(student, dict) else student for student in matching_students]

    return jsonify(matching_students)



@app.route("/delete", methods=["POST"])
def delete_data():
    del_id = request.json.get('studentId')
    students.delete_one({"_id": ObjectId(del_id)})
    
    all_students = list(students.find({}))
    
    return jsonify(all_students)


@app.route("/plot", methods=["GET"])
def plot_data():
    all_students = list(students.find({}))
    
    subjects_applied = {}
    total_gpa = 0
    males = 0
    females = 0
    
    for student in all_students:
        if student['gender'] == 'Male':
            males += 1
        else:
            females += 1
        
    for student in all_students:
        program = student.get('program')
        gpa = float(student.get('gpa'))
        
        # Count the number of applicants for each subject
        subjects_applied[program] = int(subjects_applied.get(program, 0) + 1)
        total_gpa += gpa

    
    # Plotting
    
    # plot pie chart for gender balance
    labels = ['Males', 'Females']
    sizes = [males, females]
    colors = ['#4c72b0', '#c44e52']
    explode = (0.1, 0)  

    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, explode=explode, colors=colors, autopct='%1.1f%%', startangle=90, shadow=True)
    plt.title('Gender Balance', fontweight='bold', fontsize=14)
    plt.axis('equal')
    gender_plot_path = os.path.join(app.config['STATIC_FOLDER'], 'images', 'gender_balance.png')
    plt.savefig(gender_plot_path)
    plt.close()
    
    
    # Plot bar chart for subjects applied
    plt.figure(figsize=(10, 6))
    plt.bar(subjects_applied.keys(), subjects_applied.values(), color='#4c72b0')
    plt.xlabel('Subjects', fontweight='bold', fontsize=12)
    plt.ylabel('Number of Applicants', fontweight='bold', fontsize=12)
    plt.title('Number of Applicants for Each Subject', fontweight='bold', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    subjects_plot_path = os.path.join(app.config['STATIC_FOLDER'], 'images', 'subjects_applied.png')
    plt.savefig(subjects_plot_path)
    plt.close()

    # Plot histogram for GPA distribution
    plt.figure(figsize=(10, 6))
    plt.hist([float(student.get('gpa')) for student in all_students], bins=10, color='#4c72b0', edgecolor='white')
    plt.xlabel('GPA', fontweight='bold', fontsize=12)
    plt.ylabel('Frequency', fontweight='bold', fontsize=12)
    plt.title('Distribution of GPA', fontweight='bold', fontsize=14)
    plt.xticks(np.arange(0, 5.5, 0.5))
    plt.yticks(np.arange(0, 20, 2))
    plt.grid(axis='y', alpha=0.5)
    plt.tight_layout()
    gpa_plot_path = os.path.join(app.config['STATIC_FOLDER'], 'images', 'gpa_distribution.png')
    plt.savefig(gpa_plot_path)
    plt.close()

    return render_template("index.html", subjects_plot_path=subjects_plot_path, gpa_plot_path=gpa_plot_path, gender_plot_path=gender_plot_path)
    
if __name__ == '__main__':
    app.run(debug=True , threaded=False)