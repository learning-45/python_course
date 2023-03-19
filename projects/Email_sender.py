#https://www.youtube.com/watch?v=pdy3nh1tn6I


from email.message import EmailMessage
import ssl 
import smtplib

email_sender = '190040236ece@gmail.com'
email_password = 'Naresh@236'

email_receiver = 'fekex51018@galcake.com'

subject = "This is my first project"

body = """ 

When you receive this email

"""

em = EmailMessage()
em['from'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())

