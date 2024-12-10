from flask import Flask,render_template,request,redirect
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
app = Flask(__name__)
otp = "0"
temp = 1
tasks = []
@app.route("/")
def index():
    return render_template("sample.html")

@app.route("/mainpage")
def mainpage():
    return render_template("sample3.html",tasks=tasks)

@app.route("/collectdata",methods=["POST","GET"])
def collectdata():
    name = request.form['name']
    email = request.form['email']
    print(name,email)
    global otp
    otp = str(random.randint(1111,9999))
    print(otp)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    mailusername = "tangasaikrishna82001@gmail.com"
    mailpassword =  "ohwp honk tsdw ivqo"
    from_email = "tangasaikrishna82001@gmail.com"
    to_email = email
    subject = "OTP for Verification"
    body = f"The OTP for login is {otp}"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['subject'] = subject
    msg.attach(MIMEText(body,'plain'))

    server = smtplib.SMTP(smtp_server,smtp_port)
    server.starttls()
    server.login(mailusername,mailpassword)
    server.send_message(msg)
    server.quit()
    return render_template("sample2.html",name=name,email=email)

@app.route("/verifyemail",methods=["POST","GET"])
def verifyemail():
    name = request.form['name']
    email = request.form['email']
    xotp = request.form['otp']
    print(xotp)
    if xotp == otp:
        return render_template("sample3.html",name=name,email=email)
    else:
        return "Wrong OTP ENTERED"
@app.route("/addtask",methods=["POST","GET"])
def addtask():
    global temp
    global tasks
    taskname = request.form['task']
    name = request.form['username']
    taskid = temp
    temp = temp + 1
    tasks.append({'id':str(taskid),'content':taskname})
    print(tasks)
    return render_template("sample3.html",tasks=tasks,name=name)

@app.route("/updatedata",methods=["POST","GET"])
def updatedata():
    id = request.form['updated_id']
    content = request.form['updated_task']
    name = request.form['username']
    ind = None 
    for data in tasks:
        if data['id'] == id:
            ind = tasks.index(data)
            break 
    tasks[ind]['content'] = content
    return render_template("sample3.html",tasks=tasks,name=name)

@app.route("/deletedata",methods=["POST","GET"])
def deletedata():
    id = request.form['delete_data_id']
    name = request.form['username']
    ind = None 
    for data in tasks:
        if data['id'] == id:
            ind = tasks.index(data)
            break 
    tasks.pop(ind)
    return render_template("sample3.html",tasks=tasks,name=name)
    
if __name__ == "__main__":
    app.run()
