import smtplib

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import codecs
import sys

import os

addrs = set(open(sys.argv[1]).readlines())

for i, toaddr in enumerate(addrs):
	try:
		print ("%i/%i) Sending to address: %s" % (i + 1, len(addrs), toaddr))
		fromaddr = "********************"
	 
		msg = MIMEMultipart()

		msg['From'] = fromaddr
		msg['To'] = toaddr
		msg['Subject'] = 'Junior test enginier job'

		with open('msg_text.txt', 'r') as text:
			body = MIMEText(text.read(), 'plain')
			msg.attach(body)


		for file in ['************_cv_ru.pdf', '***********_cv_en.pdf', '***********_motivation_ru.pdf', '************_motivation_en.pdf']:
			with open(file, 'rb') as fp:
				cv = MIMEBase('application', "octet-stream")
				cv.set_payload(fp.read())
				encoders.encode_base64(cv)
				cv.add_header('Content-Disposition', 'attachment', filename=file)
				msg.attach(cv)

		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.ehlo()
		s.starttls()
		s.ehlo()
		s.login(fromaddr, 'password')
		s.sendmail(fromaddr, toaddr, msg.as_string())
		s.close()
    
	except ...:
	 	print ("Failed to send to %s" % toaddr) 
