import sqlite3 

con = sqlite3.connect("students_marks.db")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS sessions")
cur.execute("DROP TABLE IF EXISTS students")

cur.execute("""
CREATE TABLE students (
    roll_no INTEGER PRIMARY KEY,
    passwd TEXT NOT NULL,
    mark INTEGER NOT NULL
)
""")

cur.execute("""
CREATE TABLE sessions (
    roll_no INTEGER NOT NULL,
    token TEXT PRIMARY KEY,
    FOREIGN KEY (roll_no)
        REFERENCES students(roll_no)
)
""")

students = [
    (1,  "pass1",  72),
    (2,  "pass2",  68),
    (3,  "pass3",  81),
    (4,  "pass4",  100),
    (5,  "pass5",  89),
    (6,  "pass6",  77),
    (7,  "pass7",  84),
    (8,  "pass8",  91),
    (9,  "pass9",  79),
    (10, "pass10", 99) 
]

cur.executemany(
    """
    INSERT INTO students
    (roll_no, passwd, mark)
    VALUES (?, ?, ?)
    """,
    students
)

con.commit()

print("Database created successfully.")
print("Inserted 10 student records.")

con.close()
