from databases import *
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html', students=query_all())

@app.route('/student/<int:student_id>')
def display_student(student_id):
	return render_template('student.html', student=query_by_id(student_id))

#Create an '/add' route here:
@app.route('/add', methods=['GET', 'POST'])
def add_student_route():
	if request.method == 'GET':
		return render_template('add.html')
	else:
		name = request.form['student_name']
		year = request.form['student_year']
		new_student = Student(name=name,
		year=year,
		finished_lab=False)
		session.add(new_student)
		session.commit()
		return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
