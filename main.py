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
def index():
    return render_template('index.html')

@app.route('/signinpt',methods = ['POST', 'GET'])
def signinpt():
    if request.method == 'POST': ##check if there is post data
        name = request.form['UName']
        pw = request.form['Password']
        print(name)
        myCursor.execute("SELECT ssn , patient.uname , patient.pass , patient.email , patient.phone , patient.address , patient.weight ,patient.entry_day , patient.disease , dr.uname FROM patient LEFT JOIN dr_patient on dr_patient.patient_ssn =patient.ssn LEFT JOIN dr ON dr.id =dr_patient.dr_id WHERE patient.uname=(\'%s\') AND patient.pass=(\'%s\')"%(name,pw))
        myResult = myCursor.fetchall()
        return render_template('profilept.html' ,doctors_data = myResult)
    else:
        return render_template('signinpt.html')

@app.route('/signindr',methods = ['POST', 'GET'])
def signindr():
    if request.method == 'POST': ##check if there is post data
        name = request.form['UName']
        pw = request.form['Password']
        myCursor.execute("SELECT id,dr.uname,dr.pass,dr.email,dr.phone,dr.address,dep_name,exp_years,patient.uname FROM dr LEFT JOIN dep on dr.depno = dep.dep_no LEFT JOIN dr_patient on dr_patient.dr_id =dr.id LEFT JOIN patient ON patient.ssn =dr_patient.patient_ssn WHERE dr.uname=(\'%s\') AND dr.pass=(\'%s\')"%(name,pw))
        myResult = myCursor.fetchall()
        return render_template('profiledr.html' ,doctors_data = myResult)
    else:
        return render_template('signindr.html')


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
            return render_template('contactus.html',message="your complain has been recorded ")
        except:
            return render_template('contactus.html',error="Something Went wrong ")
    else:
      return render_template('contactus.html')
"""
@app.route('/profiledr')
def profiledr():
    myCursor.execute("SELECT id,dr.uname,dr.pass,dr.email,dr.phone,dr.address,dep_name,exp_years,patient.uname FROM dr JOIN dep on dr.depno = dep.dep_no JOIN dr_patient on dr_patient.dr_id =dr.id JOIN patient ON patient.ssn =dr_patient.patient_ssn WHERE dr.uname='abdallah'")
    myResult = myCursor.fetchall()
    return render_template('profiledr.html' ,doctors_data = myResult)
"""
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
    if request.method == 'POST':
        d_id = request.form['doc_id']
        myCursor10 = mydb.cursor()
        sql = "SELECT id,dr.uname,dr.pass,dr.email,dr.phone,dr.address,dep_name,exp_years,patient.uname FROM dr LEFT JOIN dep on dr.depno = dep.dep_no LEFT JOIN dr_patient on dr_patient.dr_id =dr.id LEFT JOIN patient ON patient.ssn =dr_patient.patient_ssn WHERE id= %s"
        val = (d_id, )
        myCursor10.execute(sql,val)
        myResult7 =myCursor10.fetchall()
        return render_template('Adoctor.html' ,doctors_data = myResult7)
    else:
        myCursor.execute("SELECT id,dr.uname,dr.pass,dr.email,dr.phone,dr.address,dep_name,exp_years,patient.uname FROM dr LEFT JOIN dep on dr.depno = dep.dep_no LEFT JOIN dr_patient on dr_patient.dr_id =dr.id LEFT JOIN patient ON patient.ssn =dr_patient.patient_ssn")
        myResult = myCursor.fetchall()
        return render_template('Adoctor.html' ,doctors_data = myResult)

@app.route('/Dedit/<string:d_id>', methods = ['POST','GET'])
def Dedit(d_id):
    if request.method == 'POST':
        d_name2 = request.form['UName']
        d_mail2 = request.form['email']
        d_pass1_2 = request.form['password1']
        d_phone2 = request.form['phone']
        d_address2 = request.form['address']
        d_dep2 = request.form['department']
        d_exp2 = request.form['Experiance']
        print(d_id,d_mail2)
        myCursor21 = mydb.cursor()
        sql = "UPDATE dr SET uname = %s , pass = %s , email = %s , phone =%s , address =%s , depno =%s ,exp_years =%s  WHERE id = %s"
        val = (d_name2,d_pass1_2,d_mail2,d_phone2,d_address2,d_dep2,d_exp2 ,d_id)
        myCursor21.execute(sql,val)
        mydb.commit()  
        return redirect(url_for('Adoctor'))
    else:
        sql = 'SELECt * FROM dr WHERE id = %s'
        val = (d_id, )
        myCursor.execute(sql,val)
        myResult = myCursor.fetchall()
        return render_template('A_Dedit.html',doctors_data = myResult)
    

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
        sql = "SELECT ssn , patient.uname , patient.pass , patient.email , patient.phone , patient.address , patient.weight ,patient.entry_day , patient.disease , dr.uname FROM patient LEFT JOIN dr_patient on dr_patient.patient_ssn =patient.ssn LEFT JOIN dr ON dr.id =dr_patient.dr_id where ssn = %s"
        val = (p_id, )
        myCursor10.execute(sql,val)
        myResult7 =myCursor10.fetchall()
        return render_template('Apatient.html' ,patients_data = myResult7)
    else:
        myCursor.execute("SELECT ssn , patient.uname , patient.pass , patient.email , patient.phone , patient.address , patient.weight ,patient.entry_day , patient.disease , dr.uname FROM patient LEFT JOIN dr_patient on dr_patient.patient_ssn =patient.ssn LEFT JOIN dr ON dr.id =dr_patient.dr_id")
        myResult2 = myCursor.fetchall()
        return render_template('Apatient.html' , patients_data = myResult2)

@app.route('/Pedit/<string:p_ssn>', methods = ['POST','GET'])
def Pedit(p_ssn):
    if request.method == 'POST':
        p_name = request.form['UName']
        p_mail = request.form['email']
        p_pass1 = request.form['password1']
        p_phone = request.form['phone']
        p_address = request.form['address']
        p_ssn2 = request.form['ssn']
        p_weight = request.form['Weight']
        p_date = request.form['Entry-Date']
        p_disease = request.form['Disease']
        print(p_ssn2,p_mail)
        myCursor20 = mydb.cursor()
        sql = "UPDATE patient SET ssn=%s, uname = %s , pass = %s , email = %s , phone =%s , address =%s , weight =%s ,entry_day =%s ,disease = %s WHERE ssn = %s"
        val = (p_ssn2,p_name,p_pass1,p_mail,p_phone,p_address,p_weight,p_date ,p_disease ,p_ssn)
        myCursor20.execute(sql,val)
        mydb.commit()  
        return redirect(url_for('Apatient'))
    else:
        sql = 'SELECt * FROM patient WHERE ssn = %s'
        val = (p_ssn, )
        myCursor.execute(sql,val)
        myResult = myCursor.fetchall()
        return render_template('A_Pedit.html',patient_data = myResult)
    


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



@app.route('/SignUP')
def Hello225():
    return render_template('Profession.html')

@app.route('/SignUpDoc',methods= ['POST','GET'])
def SignUpDoc():
    if request.method == 'POST':
        d_name = request.form['UName']
        d_mail = request.form['email']
        d_pass1 = request.form['password1']
        d_phone = request.form['phone']
        d_address = request.form['address']
        d_dep = request.form['department']
        d_exp = request.form['Experiance']

        myCursor13 = mydb.cursor()
        sql = "INSERT INTO dr (uname,pass,email,phone,address,depno,exp_years)VALUES(%s,%s,%s,%s,%s,%s,%s)"
        val = (d_name,d_pass1,d_mail,d_phone,d_address,d_dep,d_exp)
        myCursor13.execute(sql,val)
        mydb.commit()  
        return redirect(url_for('Adoctor'))
    else:
        return render_template('Sign_Up.html')

@app.route('/SignUpPatient',methods=['POST','GET'])
def SignUpPatient():
    if request.method == 'POST':
        p_name = request.form['UName']
        p_mail = request.form['email']
        p_pass1 = request.form['password1']
        p_phone = request.form['phone']
        p_address = request.form['address']
        p_ssn = request.form['ssn']
        p_weight = request.form['Weight']
        p_date = request.form['Entry-Date']
        p_disease = request.form['Disease']
        myCursor13 = mydb.cursor()
        sql = "INSERT INTO patient (uname,pass,email,phone,address,ssn,weight,entry_day,disease)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (p_name,p_pass1,p_mail,p_phone,p_address,p_ssn,p_weight,p_date,p_disease)
        myCursor13.execute(sql,val)
        mydb.commit()  
        return redirect(url_for('Apatient'))
    else:
        return render_template('SignUp2.html')

if __name__ == '__main__':
    app.run(debug=True) # dh by run server 3la el local host bta3e

