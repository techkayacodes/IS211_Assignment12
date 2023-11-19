from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = '595-359-861'  # Change this to a random secret key

def get_db_connection():
    conn = sqlite3.connect('hw13.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    # Redirect to login page or another appropriate page as the homepage
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'password':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    quizzes = conn.execute('SELECT * FROM quizzes').fetchall()
    conn.close()

    return render_template('dashboard.html', students=students, quizzes=quizzes)

@app.route('/student/add', methods=['GET', 'POST'])
def add_student():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']

        conn = get_db_connection()
        conn.execute('INSERT INTO students (first_name, last_name) VALUES (?, ?)', (first_name, last_name))
        conn.commit()
        conn.close()

        return redirect(url_for('dashboard'))

    return render_template('add_student.html')

@app.route('/quiz/add', methods=['GET', 'POST'])
def add_quiz():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    if request.method == 'POST':
        subject = request.form['subject']
        question_count = request.form['question_count']
        quiz_date = request.form['quiz_date']

        conn = get_db_connection()
        conn.execute('INSERT INTO quizzes (subject, question_count, quiz_date) VALUES (?, ?, ?)', (subject, question_count, quiz_date))
        conn.commit()
        conn.close()

        return redirect(url_for('dashboard'))

    return render_template('add_quiz.html')

@app.route('/student/<int:student_id>')
def student_results(student_id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    conn = get_db_connection()
    results = conn.execute('SELECT * FROM results WHERE student_id = ?', (student_id,)).fetchall()
    conn.close()

    return render_template('student_results.html', results=results, student_id=student_id)

if __name__ == '__main__':
    app.run(debug=True)
