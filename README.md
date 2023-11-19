# IS211_Assignment12
IS211_Assignment12

# School Management System

This Flask-based web application is designed to manage student and quiz data for a school. It allows teachers to log in, view student details, quizzes, and manage quiz results.

## Features

- User authentication for teachers.
- View lists of students and quizzes.
- Add new students and quizzes.
- View quiz results for each student.

## Setup and Installation

To get this application running on your local machine, follow these steps:

1. **Clone the Repository** (if applicable):
   ```bash
   git clone [repository-url]
   cd IS211_Assignment12
Install Flask:
If you haven't installed Flask, do it using pip:

bash
Copy code
pip install Flask
Initialize the Database:
Run the initialize-app.py script to set up the SQLite database:

bash
Copy code
python initialize-app.py
Run the Application:
Start the Flask application by running:

bash
Copy code
flask run
Usage
Logging In
To log in to the application:

Navigate to http://127.0.0.1:5000/login in your web browser.
Use the following credentials:
Username: admin
Password: password
Upon successful login, you will be redirected to the dashboard.
Dashboard
On the dashboard, you can view lists of students and quizzes. You also have options to add new students, add new quizzes, and view quiz results for each student.