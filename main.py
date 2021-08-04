from background import draw_background
from studentspiral import student_drawing
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from tkinter import *
import keyring
import smtplib, ssl
import subprocess
import turtle


FILE_NAME = ""
STUDENT_EMAIL = ""

screen = turtle.Screen()
screen.bgcolor("#0E635E")
turtle.speed(0)
draw_background()

student_drawing()

turtle.ht()

screen.getcanvas().postscript(file=f"{FILE_NAME}.eps")

subprocess.run(["inkscape", f"--export-filename=images/{FILE_NAME}.svg", f"{FILE_NAME}.eps"])
subprocess.run(["rm", f"{FILE_NAME}.eps"])
subprocess.run(["inkscape", f"images/{FILE_NAME}.svg"])

# Set up credentials
smtp_server = 'smtp.gmail.com'
smtp_port = 587
WORK_GMAIL = 'russell.helmstedter@venturaedu.org'
PASSWORD = keyring.get_password("system", "venturaedu")

# Set up message
message = MIMEMultipart('mixed')
message['From'] = f'Contact <{WORK_GMAIL}>'
message['To'] = STUDENT_EMAIL
message['Subject'] = 'High Resolution Turtle Graphic'

# Write the email
msg_content = '<p>Hello,<br>Here is your drawing as a high resolution svg file. I hope you enjoy.<br><br>Mr. Helmstedter</p><br>'
body = MIMEText(msg_content, 'html')
message.attach(body)

# Find and attachment image
attachmentPath = f"images/{FILE_NAME}.svg"
try:
	with open(attachmentPath, "rb") as attachment:
		p = MIMEApplication(attachment.read(),_subtype="svg")	
		p.add_header('Content-Disposition', "attachment; filename= %s" % attachmentPath.split("/")[-1]) 
		message.attach(p)
except Exception as e:
	print(str(e))

# Send email
msg_full = message.as_string()
context = ssl.create_default_context()

with smtplib.SMTP(smtp_server, smtp_port) as server:
	server.ehlo()  
	server.starttls(context=context)
	server.login(WORK_GMAIL, PASSWORD)
	server.sendmail(WORK_GMAIL, message['To'], msg_full)
	server.quit()

print("email sent out successfully")


