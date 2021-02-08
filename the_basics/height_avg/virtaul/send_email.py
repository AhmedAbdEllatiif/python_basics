from email.mime.text import MIMEText
import smtplib

def send_email(email,height,avg_h,count):
    from_email = "testingpurpose2307@gmail.com"
    from_password = 'A@123456789'
    to_email = email
    
    subject = ("Height data")
    avg_h = round(avg_h,1)
    message = "<h2 style=\"text-align:center;\">Average Human Height</h2>  <p style=\"text-align:center;\">Hey there, your height is <strong>{}</strong>. <br> The Average is <strong>{}</strong> <br> Total <strong>{}</strong>. <br> <strong>Thanks!</strong> </p> ".format(height,avg_h,count)
    
    msg = MIMEText(message,'html')
    
    msg['Subject'] = subject
    msg["To"] = to_email
    msg["from"] = from_email 
    
    gmail = smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)
    
    
    