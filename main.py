import smtplib
import imghdr
from email.message import EmailMessage



message = EmailMessage()
message['Subject'] = 'Ssup boli!!!!!!   ' //subject
message['From'] = maildid
message['To'] = 'sharansk792000@gmail.com'
message.set_content('Hello Boli!!!!!!') // message
files = []

for file in files:
    

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(maildid, password)
    
    smtp.send_message(message)