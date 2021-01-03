from flask import Flask, render_template ,request,url_for,redirect,flash #import flask class

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
    if request.method == 'POST':
        d_id = request.form['doc_id']
        myCursor10 = mydb.cursor()
        sql = "SELECT id,dr.uname,dr.pass,dr.email,dr.phone,dr.address,dep_name,exp_years,patient.uname FROM dr JOIN dep on dr.depno = dep.dep_no JOIN dr_patient on dr_patient.dr_id =dr.id JOIN patient ON patient.ssn =dr_patient.patient_ssn WHERE id= %s"
        val = (d_id, )
        myCursor10.execute(sql,val)
        myResult7 =myCursor10.fetchall()
        return render_template('Adoctor.html' ,doctors_data = myResult7)
    else:
        myCursor.execute("SELECT id,dr.uname,dr.pass,dr.email,dr.phone,dr.address,dep_name,exp_years,patient.uname FROM dr JOIN dep on dr.depno = dep.dep_no JOIN dr_patient on dr_patient.dr_id =dr.id JOIN patient ON patient.ssn =dr_patient.patient_ssn")
        myResult = myCursor.fetchall()
        return render_template('Adoctor.html' ,doctors_data = myResult)

@app.route('/Dedit')
def Dedit():
    return render_template('Dedit.html')

@app.route('/Ddelete/<string:dr_id>', methods = ['GET'])
def delete(dr_id):
    # flash("Record Has Been Deleted Successfully")
    myCursor15 = mydb.cursor()
    sql = "DELETE FROM dr WHERE id = %s"
    val = (dr_id, )
    myCursor15.execute(sql,val)

    mydb.commit()
    
    return redirect(url_for('Adoctor'))


@app.route('/Apatient',methods =['POST','GET']) 
def Apatient():
    if request.method == 'POST':
        p_id = request.form['p_id']
        myCursor10 = mydb.cursor()
        sql = "SELECT ssn , patient.uname , patient.pass , patient.email , patient.phone , patient.address , patient.weight ,patient.entry_day , patient.disease , dr.uname FROM patient JOIN dr_patient on dr_patient.patient_ssn =patient.ssn JOIN dr ON dr.id =dr_patient.dr_id where ssn = %s"
        val = (p_id, )
        myCursor10.execute(sql,val)
        myResult7 =myCursor10.fetchall()
        return render_template('Apatient.html' ,patients_data = myResult7)
    else:
        myCursor.execute("SELECT ssn , patient.uname , patient.pass , patient.email , patient.phone , patient.address , patient.weight ,patient.entry_day , patient.disease , dr.uname FROM patient JOIN dr_patient on dr_patient.patient_ssn =patient.ssn JOIN dr ON dr.id =dr_patient.dr_id")
        myResult2 = myCursor.fetchall()
        return render_template('Apatient.html' , patients_data = myResult2)

@app.route('/Pedtit')
def Pedit():
    return render_template('Pedit.html')

@app.route('/Pdelete/<string:p_id>', methods = ['GET'])
def Pdelete(p_id):
    myCursor16 = mydb.cursor()
    sql = "DELETE FROM patient WHERE ssn = %s"
    val = (p_id, )
    myCursor16.execute(sql,val)
    mydb.commit()
    
    return redirect(url_for('Apatient'))


@app.route('/Acomplains') 
def Acomplains():
    myCursor.execute("SELECT * FROM contact_us")
    myResult5 = myCursor.fetchall()
    return render_template('Acomplains.html' ,complains_data = myResult5)


if __name__ == '__main__':
    app.run() # dh by run server 3la el local host bta3e

