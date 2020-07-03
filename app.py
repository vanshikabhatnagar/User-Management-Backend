from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

mysql = MySQL(app)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_DB'] = 'user_mgmt'
app.config['MYSQL_PASSWORD'] = 'lakshay'


@app.route('/')
def hello_world():
    return 'This is the backend for User Management System'


# EMPLOYEE

@app.route('/employee/get')
def getEmp():
    cur = mysql.connection.cursor()
    query = "SELECT * FROM employee"
    cur.execute(query)
    res = cur.fetchall()
    return str(res)


@app.route('/employee/get/<id>')
def getEmpById(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM employee where empID=%s' % (id))
    res = cur.fetchone()
    return str(res)


@app.route('/employee/remove/<id>', methods=['POST'])
def removeEmpById(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('delete FROM employee where empID=%s' % (id))
        mysql.connection.commit()
        return "successful"
    except Exception as e:
        return "unsuccessful"+str(e)


@app.route('/employee/insert', methods=['POST'])
def insertEmp():
    try:
        empID = request.json['empID']
        name = request.json['name']
        email = request.json['email']
        dob = request.json['dob']
        doj = request.json['doj']
        dept = request.json['dept']
        phone = request.json['phone']
        desig = request.json['desig']
        hours = request.json['hours']
        otime = request.json['otime']
        paid = request.json['paid']
        unpaid = request.json['unpaid']
        med = request.json['med']
        comp = request.json['comp']
        cursor = mysql.connection.cursor()
        query = 'insert into employee values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s , %s, %s, %s)'
        toPut = (empID, name, email, dob, doj, dept, phone,
                 desig, hours, otime, paid, unpaid, med, comp)
        cursor.execute(query, toPut)
        mysql.connection.commit()
        return "successful"
    except Exception as e:
        return "unsuccessful"+str(e)


# INVESTOR

@app.route('/investors/get')
def getInv():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM investors')
    res = cur.fetchall()
    return str(res)


@app.route('/investors/get/<id>')
def getInvById(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM investors where invID=%s' % (id))
    res = cur.fetchone()
    return str(res)


@app.route('/investors/remove/<id>', methods=['POST'])
def removeInvById(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('delete FROM investors where invID=%s' % (id))
        mysql.connection.commit()
        return "successful"
    except Exception as e:
        return "unsuccessful"+str(e)


@app.route('/investors/insert', methods=['POST'])
def insertInv():
    try:
        invID = request.json['invID']
        name = request.json['name']
        email = request.json['email']
        doi = request.json['doi']
        amt = request.json['amt']
        per = request.json['per']
        validity = request.json['validity']
        phone = request.json['phone']

        cursor = mysql.connection.cursor()
        query = 'insert into investors values (%s, %s, %s, %s, %s, %s, %s, %s)'
        toPut = (invID, name, email, doi, amt, per, validity, phone)
        cursor.execute(query, toPut)
        mysql.connection.commit()
        return "successful"
    except Exception as e:
        return "unsuccessful"+str(e)

# ADMIN


@app.route('/admin/get')
def getAdmin():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM admin')
    res = cur.fetchall()
    return jsonify(res)


@app.route('/admin/get/<id>')
def getAdminById(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM admin where admID=%s' % (id))
    res = cur.fetchone()
    return str(res)


@app.route('/admin/remove/<id>', methods=['POST'])
def removeAdminById(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('delete FROM admin where admID=%s' % (id))
        mysql.connection.commit()
        return "successful"
    except Exception as e:
        return "unsuccessful"+str(e)


@app.route('/admin/insert', methods=['POST'])
def insertAdmin():
    try:
        admID = request.json['admID']
        name = request.json['name']
        email = request.json['email']
        phone = request.json['phone']

        cursor = mysql.connection.cursor()
        query = 'insert into admin values (%s, %s, %s, %s)'
        toPut = (admID, name, email, phone)
        print(query, toPut)
        cursor.execute(query, toPut)

        mysql.connection.commit()
        return "successful"
    except Exception as e:
        return "unsuccessful"+str(e)
