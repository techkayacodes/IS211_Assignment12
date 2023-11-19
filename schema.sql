CREATE TABLE Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

CREATE TABLE Quizzes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT NOT NULL,
    question_count INTEGER NOT NULL,
    quiz_date DATE NOT NULL
);

CREATE TABLE Results (
    student_id INTEGER,
    quiz_id INTEGER,
    score INTEGER,
    FOREIGN KEY (student_id) REFERENCES Students(id),
    FOREIGN KEY (quiz_id) REFERENCES Quizzes(id)
);
