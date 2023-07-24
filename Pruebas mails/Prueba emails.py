import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ACCOUNT = os.environ.get("EMAIL_USER")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")

contacts = ["examplemail1@gmail.com", "examplemail2@gmail.com"]
files = ["Pruebas mails\img\canelones.png"]

for contact in contacts:
	msg = EmailMessage()
	msg["subject"] = "Viandas de comida casera a domicilio"
	msg["From"] = EMAIL_ACCOUNT
	msg["To"] = contact
	
	# Contenido de ejemplo
	msg.set_content("""\
¡Hola!

Somos Benito's, un emprendimiento de comida casera localizado en CABA. Realizamos viandas por encargo. Si desea comer algo rico no dude en contactarnos:

Gracias por su atención,

Benito's""")

	for file in files:
		with open(file, "rb") as f:
			file_data = f.read()
			file_type = imghdr.what(f.name)
			file_name = f.name

		msg.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_name)

	with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
		smtp.login(EMAIL_ACCOUNT,EMAIL_PASSWORD)

		smtp.send_message(msg)

	print("Email sent to:", contact)