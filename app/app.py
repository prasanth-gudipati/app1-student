from flask import Flask, render_template, request, redirect
from db import students

app = Flask(__name__)

def generate_student_id():
    last = students.find_one(sort=[("student_id", -1)])
    return (last["student_id"] + 1) if last else 10001

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/students')
def show_students():
    all_students = list(students.find({}, {'_id': 0}))
    return render_template('show_students.html', students=all_students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        data = request.form
        new_student = {
            "student_id": generate_student_id(),
            "first_name": data['first_name'],
            "last_name": data['last_name'],
            "dob": data['dob'],
            "address": data['address'],
            "middle_name": data.get('middle_name', ''),
            "sex": data.get('sex', '')
        }
        students.insert_one(new_student)
        return redirect('/students')
    return render_template('add_student.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete_student():
    if request.method == 'POST':
        sid = request.form.get('student_id')
        fname = request.form.get('first_name')
        lname = request.form.get('last_name')

        if sid:
            students.delete_one({"student_id": int(sid)})
        elif fname and lname:
            students.delete_one({"first_name": fname, "last_name": lname})
        return redirect('/students')
    return render_template('delete_student.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
