import smtplib
import imghdr
import os
import pandas as pd
from email.message import EmailMessage

path = "attachments"
files = []
attachments = os.listdir(path)

for file in range(len(attachments)):
    files.append(f'{path}/{attachments[file]}')

cont = pd.read_excel("contacts.xlsx")
contacts = cont['mail id'].values
print(contacts)

contacts = [maildid, 'swaasthik.shetty1@gmail.com'] 
message = EmailMessage()
message['Subject'] = 'Ssup boli!!!!!!   ' 
message['From'] = maildid
message['To'] = contacts
message.set_content('Hello Boli!!!!!!') 

message.add_alternative("""\
    <!DOCTYPPE html>
    <html>
    <body>
    <h1 >Hello destooooo!!!!!</h1>
    </body>
    </html>            
                        """, subtype='html')

# files = ['./attachments/1.jpg', './attachments/4.pdf']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
    message.add_attachment(file_data, maintype='application', subtype='octect-stream', filename= file_name)
    

# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#     smtp.login(maildid, password)
#     smtp.send_message(message)