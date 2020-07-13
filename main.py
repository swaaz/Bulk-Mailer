import smtplib
import imghdr
import os
import pandas as pd
from email.message import EmailMessage

# your account credentials
maildid = ""  #enter your email id here
password = "" #enter your password here

files = []

# path of the folder which will be attached
path = "attachments" 
attachments = os.listdir(path)

# creating a new list to store files along with path
for file in range(len(attachments)):
    files.append(f'{path}/{attachments[file]}')

# reading mail id's from excel sheet
cont = pd.read_excel("contacts.xlsx")
contacts = cont['mail id'].values  #storing all the mail id's in contacts list


for contact in contacts:
    message = EmailMessage()
    message['From'] = maildid
    message['To'] = contact
    message['Subject'] = 'Enter the Subject here' #replace the subject  
    
    """
    Note: if you want to send mail with content then use option 1 and delete the option 2
          or
          if you want to send HTML mail then use option 2 and delete option 1
    """
    
    # option 1
    message.set_content('Enter the content here ') #this is optional. if you are using web mails then this is not necessary.

    # option 2
    message.add_alternative("""\    
        <!DOCTYPPE html>
            <html>
                <body>
                
                    //Insert you html code here
                    
                </body>
            </html>            
                            """, subtype='html')
    

    # attaching files to the mail
    for file in files:
        with open(file, 'rb') as f:
            file_data = f.read()
            file_type = imghdr.what(f.name)
            file_name = f.name
        message.add_attachment(file_data, maintype='application', subtype='octect-stream', filename= file_name)
        
    # Sending mails
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(maildid, password)
        smtp.send_message(message)
        
        # if the mail is Successfully sent then this statement will be printed
        print("Mail sent Successfully to {}".format(contact))
        
print("\nSuccessfully sent!!!")