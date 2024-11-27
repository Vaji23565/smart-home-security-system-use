import smtplib
from email.message import EmailMessage

def email_alert(subject,body,to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject']=subject
    msg['to'] =to
    msg['from']="ramya.devtest.mail@gmail.com"
    user="ramya.devtest.mail@gmail.com"
    password="wjgfyarvwubrpuss"

    server= smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
    server.quit()

if __name__== '__main__':
    email_alert("testmail","this is test mail","ramyaravi654@gmail.com")
