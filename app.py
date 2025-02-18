#  ========================================== IMPORTS ==========================================
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from datetime import date
from flask_cors import CORS
import logging
import sys
import mysql.connector
from os import environ
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,jwt_optional,
    get_jwt_identity
)

# ========================================== CONFIG SETTINGS ==========================================
#  INITIALISE FLASK APP
app = Flask(__name__)

# ----> MySQL Server to use <----
# sqlServer = "remote"
# sqlServer = "local"
sqlServer = "heroku"

# Mode: development OR production
processEnv = app.config['ENV']


# Enable CORS
CORS(app)
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# PRODUCTION
if(processEnv == "production"):
    # USE HEROKU
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
    app.config['MYSQL_USER'] = environ.get('MYSQL_USER')
    app.config['MYSQL_HOST'] = environ.get('MYSQL_HOST')
    app.config['MYSQL_DB'] = environ.get('MYSQL_DB')
    app.config['MYSQL_PASSWORD'] = environ.get('MYSQL_PASSWORD')
    app.config['JWT_SECRET_KEY'] = environ.get('JWT_SECRET_KEY')

# DEVELOPMENT
else:

    # =========================== LOCAL SQL SERVER ===========================
    # if(sqlServer == "local"):
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_HOST'] = '127.0.0.1'
    app.config['MYSQL_DB'] = 'user_mgmt'
    app.config['MYSQL_PASSWORD'] = 'lakshay'
    app.config['JWT_SECRET_KEY'] = '80NwB9CS03OzSND1HQY2Q3NF1S6P5sg2AWY9LRITXYddf8NTPY'
    # =========================== HEROKU SQL SERVER ===========================
    # else:
    #     app.config.from_object('config')
    #     # Enable Logging for Heroku
    #     app.logger.addHandler(logging.StreamHandler(sys.stdout))
    #     app.logger.setLevel(logging.ERROR)

jwt = JWTManager(app)
mysql = MySQL(app)


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
    return jsonify(res)


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
    return jsonify(res)


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


@app.route('/auth', methods=['POST'])
def auth():
    try:
        userID = request.json['userID']
        password = request.json['password']
        cursor = mysql.connection.cursor()
        query = 'select password from userpasswords where id=%s'%(userID)
        print(query)
        cursor.execute(query)
        res = cursor.fetchone()
        if(res is not None and res['password']==password):
            return jsonify({'message':'Logged in successfully'}),200
        else:
            return jsonify({'message':'Wrong Password'}), 401
    except Exception as e:
        return "unsuccessful"+str(e)


# Working
@app.route('/login', methods=['POST'])
@jwt_optional
def login():
    userID = get_jwt_identity()
    if(userID):
        access_token = create_access_token(identity=userID)
        return jsonify({'message':'Logged in successfully','access_token':access_token}),200
    cursor = mysql.connection.cursor()
    userID = request.json['userID']
    password = request.json['password']
    query = 'select password from userpasswords where id=%s'%(userID)
    try: 
        cursor.execute(query)
        res = cursor.fetchone()
        if(res is not None and res['password']==password):
            access_token = create_access_token(identity=userID)
            return jsonify({'message':'Logged in successfully','access_token':access_token}),200
        else:
            return jsonify({'message':'Wrong Password'}), 401
    except Exception as e:
        return jsonify({'Error': 'True','message': str(e)}), 400