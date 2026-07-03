from flask import Flask, request, make_response, jsonify
import sqlite3
import secrets


app = Flask(__name__)
con = sqlite3.connect("students_marks.db", check_same_thread=False)
cur = con.cursor()

@app.route("/login", methods=['POST'])
def login():
    data = request.json
    roll = data["rollno"]
    passwd = data["password"]
    # we use format strings instead of Parametized strings
    cur.execute(
        f"SELECT * FROM students WHERE roll_no = {roll} AND passwd = '{passwd}'", 
    )
    row = cur.fetchone()
    if not row:
        return jsonify({"error":"invalid credentials"}), 401

    token = secrets.token_hex(32)

    try:
        cur.execute(
            f"DELETE FROM sessions WHERE roll_no = {roll}"
        )
        cur.execute(
            f"INSERT INTO sessions (roll_no, token) VALUES ({roll}, ?)",
            (token, )
        )
        con.commit()        
    except Exception as e:
        con.rollback()
        return jsonify({"error": str(e)}), 500

    resp = make_response(
        jsonify({
            "message":"Login OK"
        })
    )
    resp.set_cookie("session_token", token, httponly=True, max_age=7200)
    
    return resp

@app.route("/my-mark", methods=['GET'])
def get_marks():
    token = request.cookies.get("session_token")
    if not token:
        return jsonify({"error":"No Session"}), 401
    cur.execute(
        "SELECT students.roll_no, students.mark FROM students JOIN sessions \
         ON students.roll_no = sessions.roll_no WHERE token = ?",
         (token, )
    )
    mark = cur.fetchone()
    if not mark :
        return jsonify({"error" : "Invalid Session"}), 401
    student_mark = mark[1]
    student_roll = mark[0]

    return jsonify({
        "roll_no" : student_roll,
        "mark" : student_mark
    })

if __name__ == "__main__":
    app.run(debug=True)