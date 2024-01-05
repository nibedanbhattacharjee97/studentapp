from flask import Flask, app, render_template
import cx_Oracle
app = Flask(__name__)
def connection():
    h = 'localhost' #Your host name/ip
    p = '1521' #Your port number
    sid = 'xe' #Your sid
    u = 'scott' #Your login user name
    pw = 'tiger' #Your login password
    d = cx_Oracle.makedsn(h, p, sid=sid)
    conn = cx_Oracle.connect(user=u, password=pw, dsn=d)
    return conn

@app.route("/")
def main():
    stus = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM STUDENT")
    for row in cursor.fetchall():
        stus.append({"STUDENT_ID": row[0], "CONTACTABLE": row[1], "CLASS_STARTED": row[2], "AE_VERIFIED": row[3]})
    conn.close()
    return render_template("stulist.html", stus = stus)


if(__name__ == "__main__"):
    app.run(debug=True)