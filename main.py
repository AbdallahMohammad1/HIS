from flask import Flask, render_template ,request,url_for #import flask class

import mysql.connector
mydb = mysql.connector.connect(
    host = 'sql7.freemysqlhosting.net',
    user = 'sql7384553',
    passwd = 'EBclWXd7nQ',
    database = 'sql7384553'
)
myCursor = mydb.cursor()

app = Flask(__name__) 
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signindr')
def signindr():
    return render_template('signindr.html')

@app.route('/signinpt')
def signinpt():
    return render_template('signinpt.html')

@app.route('/contactus',methods = ['POST', 'GET'])
def contact():
    if request.method == 'POST': ##check if there is post data
        name = request.form['name']
        try:
            #print(name)
            mydb = mysql.connector.connect(
            host = 'sql7.freemysqlhosting.net',
            user = 'sql7384553',
            passwd = 'EBclءWXd7nQ',
            database = 'sql7384553'
            )
            mc = mydb.cursor()
            #sql = "INSERT INTO contact_us (complain_text) VALUES (name)"
            mc.execute('INSERT INTO %s (complain_text) VALUES (\'%s\')' % ('contact_us', name))
            mydb.commit()
            print(name)
            return render_template('contactus.html',message="Welcome Doctor "+name)
        except:
            return render_template('contactus.html',error="Something Went wrong ")
    else:
      return render_template('contactus.html')

@app.route('/admin')
def Aindex():

    myCursor.execute("SELECT id FROM dr")
    myResult3 = myCursor.fetchall()

    myCursor2 = mydb.cursor()
    myCursor2.execute("SELECT ssn FROM patient")
    myResult4 = myCursor2.fetchall()
    
    myCursor3 = mydb.cursor()
    myCursor3.execute("SELECT * FROM contact_us")
    myResult6 = myCursor3.fetchall()
    return render_template('Aindex.html', doctors_no = myCursor.rowcount ,p_no =myCursor2.rowcount,comp_no =myCursor3.rowcount)


@app.route('/Adoctor',methods = ['POST', 'GET'])
def Adoctor():

    myCursor.execute("SELECT id,dr.uname,dr.pass,dr.email,dr.phone,dr.address,dep_name,exp_years,patient.uname FROM dr JOIN dep on dr.depno = dep.dep_no JOIN dr_patient on dr_patient.dr_id =dr.id JOIN patient ON patient.ssn =dr_patient.patient_ssn")
    myResult = myCursor.fetchall()
    return render_template('Adoctor.html' ,doctors_data = myResult)

@app.route('/Dedit')
def Dedit():
    return render_template('Dedit.html')

@app.route('/Ddelete')
def Ddelete():
    doc_id = request.args.get("dr_id")

    # sql = "DELETE FROM dr WHERE id = %s"
    # id = (doc_id, )

    # mycursor.execute(sql, id)

    # mydb.commit()

    print(doc_id, "   record(s) deleted")
    return render_template('Adoctor.html')


@app.route('/Apatient') 
def Apatient():
    myCursor.execute("SELECT ssn , patient.uname , patient.pass , patient.email , patient.phone , patient.address , patient.weight ,patient.entry_day , patient.disease , dr.uname FROM patient JOIN dr_patient on dr_patient.patient_ssn =patient.ssn JOIN dr ON dr.id =dr_patient.dr_id")
    myResult2 = myCursor.fetchall()
    return render_template('Apatient.html' , patients_data = myResult2)

@app.route('/Pedtit')
def Pedit():
    return render_template('Pedit.html')

@app.route('/Pdelete')
def Pdelete():
    sql = "INSERT INTO doctors (name,departement,id) VALUES(%s,%s,%s)"
    value = (name ,departement,id)
    myCursor.execute(sql,value)
    mydb.commit()
    return render_template('patient.html')


@app.route('/Acomplains') 
def Acomplains():
    myCursor.execute("SELECT * FROM contact_us")
    myResult5 = myCursor.fetchall()
    return render_template('Acomplains.html' ,complains_data = myResult5)

@app.route('/Cedtit')
def Cedit():
    return render_template('Cedit.html')

@app.route('/Cdelete')
def Cdelete():
    sql = "INSERT INTO doctors (name,departement,id) VALUES(%s,%s,%s)"
    value = (name ,departement,id)
    myCursor.execute(sql,value)
    mydb.commit()
    return render_template('complains.html')



if __name__ == '__main__':
    app.run() # dh by run server 3la el local host bta3e

