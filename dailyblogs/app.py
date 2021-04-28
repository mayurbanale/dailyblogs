from flask import Flask, render_template, redirect, url_for, request, session
import pymysql
app = Flask(__name__)
app.secret_key = 'hello'


@app.route('/')
def home():
    return render_template('registration.html')


@app.route('/Rinsert', methods=["POST", "GET"])
def reg():

    User = request.form['name']
    Email = request.form['email']
    Pass = request.form['pswd1']
    Cpass = request.form['pswd2']
    servername = "localhost"
    username = "root"
    password = ""
    dbname = "Dailyblogs"
    try:
        db = pymysql.connect(servername, username, password, dbname)
        cu = db.cursor()
        sql = "insert into registration(User,Email,Pass,Cpass)values('{}','{}','{}','{}')".format(
            User, Email, Pass, Cpass)
        cu.execute(sql)
        db.commit()
        return redirect('/login')
    except Exception:
        db.rollback()
        return "Error in Try: block!"


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/linsert', methods=["GET", "POST"])
def login_validation():
    servername = "localhost"
    username = "root"
    password = ""
    dbname = "Dailyblogs"
    email = request.form.get('email')
    password = request.form.get('password')
    db = pymysql.connect(servername, username, password, dbname)
    cursor.execute(
        """SELECT * FROM `users` WHERE `Email` LIKE '{}' AND `Cpass` LIKE '{}'""".format(Email, Cpass))
    users = cursor.fetchall()
    if len(users) > 0:
        session['user_id'] = users[0][0]
        return redirect('/home')
    else:
        return redirect('/')


'''
def log():
    servername = "localhost"
    username = "root"
    password = ""
    dbname = "Dailyblogs"
    try:
        if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
            Email = request.form['email']
            password = request.form['password']
            db = pymysql.connect(servername, username, password, dbname)
            cu = db.cursor()
            sql = 'SELECT * FROM registration WHERE Email = {} and Cpass = {}'.format(
                Email, Cpass)
            cu.execute(sql)
            db.commit()
            account = cu.fetchall()
            if account:
                session['loggedin'] = True
                session['Email'] = account['Email']
                session['password'] = account['Cpass']
                msg = 'Logged in successfully !'
                return redirect('/index')
            else:
                msg = 'Incorrect username/password!'

                return render_template('login.html')
    except Exception as e:
        return "error in try block" + str(e)
'''


@ app.route('/addpost')
def post():
    return render_template('Posts.html')


@ app.route('/postinsert', methods=['GET', 'POST'])
def postinsert():
    Titlename = request.form['titlename']
    Date = request.form['date']
    Subject = request.form['subject']
    servername = "localhost"
    username = "root"
    password = ""
    dbname = "Dailyblogs"
    try:
        db = pymysql.connect(servername, username, password, dbname)
        cu = db.cursor()
        sql = "insert into posts(Titleheading,Date,Subject)values('{}','{}','{}')".format(
            Titlename, Date, Subject)
        cu.execute(sql)
        db.commit()
        return redirect('/index')
    except Exception:
        db.rollback()
        return "Error in try block...!"


@app.route('/index')
def display():
    servername = "localhost"
    username = "root"
    password = ""
    dbname = "Dailyblogs"
    try:
        db = pymysql.connect(servername, username, password, dbname)
        cu = db.cursor()
        sql = "select * from posts"
        cu.execute(sql)
        data = cu.fetchall()
        return render_template('index.html', d=data)
    except Exception:
        db.rollback()
        return "Error in try block...!"


@ app.route('/delete/<id>')
def delete(id):
    servername = "localhost"
    username = "root"
    password = ""
    dbname = "Dailyblogs"
    try:
        db = pymysql.connect(servername, username, password, dbname)
        cu = db.cursor()
        sql = "delete from posts where id={}".format(id)
        cu.execute(sql)
        db.commit()
        return redirect('/index')
    except Exception:
        db.rollback()
        return " Error in  try block...!"


@ app.route('/Edit/<id>')
def edit(id):
    servername = "localhost"
    username = "root"
    password = ""
    dbname = "Dailyblogs"
    try:
        db = pymysql.connect(servername, username, password, dbname)
        cu = db.cursor()
        sql = "select * from posts where id={}".format(id)
        cu.execute(sql)
        data = cu.fetchone()
        return render_template('Edit.html', d=data)
    except Exception:
        db.rollback()
        return "Error in try block"


@app.route('/Update', methods=['GET', 'POST'])
def update():
    Titlename = request.form['titlename']
    Date = request.form['date']
    Subject = request.form['subject']
    id = request.form['id']
    servername = "localhost"
    username = "root"
    password = ""
    dbname = "Dailyblogs"
    try:
        db = pymysql.connect(servername, username, password, dbname)
        cu = db.cursor()
        sql = "UPDATE posts SET Titleheading='{}',Date='{}',Subject='{}' WHERE id={}".format(
            Titlename, Date, Subject, id)
        cu.execute(sql)
        db.commit()
        return redirect('/index')

        return "succesfully conected"
    except Exception as e:

        return "failed to update"+str(e)


app.debug = True
app.run()
