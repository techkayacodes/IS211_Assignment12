import sqlite3

def initialize_database():
    conn = sqlite3.connect('hw13.db')
    cursor = conn.cursor()

    # Create tables
    with open('schema.sql', 'r') as f:
        cursor.executescript(f.read())

    # Insert initial data
    cursor.execute("INSERT INTO students (first_name, last_name) VALUES (?, ?)", ("John", "Smith"))
    cursor.execute("INSERT INTO quizzes (subject, question_count, quiz_date) VALUES (?, ?, ?)", ("Python Basics", 5, "2015-02-05"))
    cursor.execute("INSERT INTO results (student_id, quiz_id, score) VALUES (?, ?, ?)", (1, 1, 85))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_database()
