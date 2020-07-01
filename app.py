from flask import Flask, request
from flask_mysqldb import MySQL


app = Flask(__name__)
mysql = MySQL(app)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_DB'] = 'user_mgmt'
app.config['MYSQL_PASSWORD'] = 'vanshika'


@app.route('/')
def hello_world():
    return 'This is the backend for User Management System'


@app.route('/getEmp')
def getEmp():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM employee')
    res = cur.fetchall()
    return str(res)


@app.route('/getEmp/<id>')
def getEmpById(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM employee where empID=%s' % (id))
    res = cur.fetchone()
    return str(res)


@app.route('/getInv')
def getInv():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM investors')
    res = cur.fetchall()
    return str(res)


@app.route('/getInv/<id>')
def getInvById(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM investors where invID=%s' % (id))
    res = cur.fetchone()
    return str(res)


@app.route('/getAdmin')
def getAdmin():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM admin')
    res = cur.fetchall()
    return str(res)


@app.route('/getAdm/<id>')
def getAdminById(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM admin where admID=%s' % (id))
    res = cur.fetchone()
    return str(res)


@app.route('/removeEmp/<id>', methods=['POST'])
def removeEmpById(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('delete FROM employee where empID=%s' % (id))
        mysql.connection.commit()
        return "successful"
    except Exception as e:
        return "unsuccessful"+str(e)


@app.route('/removeInv/<id>', methods=['POST'])
def removeInvById(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('delete FROM investors where invID=%s' % (id))
        mysql.connection.commit()
        return "successful"
    except Exception as e:
        return "unsuccessful"+str(e)


@app.route('/removeAdmin/<id>', methods=['POST'])
def removeAdminById(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('delete FROM admin where admID=%s' % (id))
        mysql.connection.commit()
        return "successful"
    except Exception as e:
        return "unsuccessful"+str(e)


@app.route('/insertEmp', methods=['POST'])
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


@app.route('/insertInv', methods=['POST'])
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


@app.route('/insertAdmin', methods=['POST'])
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
