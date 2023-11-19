import sqlite3

def initialize_db():
    conn = sqlite3.connect('hw13.db')
    with open('schema.sql') as f:
        conn.executescript(f.read())

    cur = conn.cursor()

    # Insert sample data
    cur.execute("INSERT INTO Students (first_name, last_name) VALUES (?, ?)", ('John', 'Smith'))
    cur.execute("INSERT INTO Quizzes (subject, question_count, quiz_date) VALUES (?, ?, ?)", ('Python Basics', 5, '2015-02-05'))
    cur.execute("INSERT INTO Results (student_id, quiz_id, score) VALUES (?, ?, ?)", (1, 1, 85))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    initialize_db()
