import smtplib


my_email = "asweny2@gmail.com"
to_email = "andrea.sweny@gmail.com"


gmail_smtp = "smtp.gmail.com"  # Simple Mail Transfer Protocol
# pwd = "wvnu kycv yjhs wysp"
pwd = "sdoa evta rnnn xqkh"
connection = smtplib.SMTP(gmail_smtp, port=587)

connection.starttls()  # Transport Layer Security
connection.login(user=my_email, password=pwd)
msg_body = "Here's an electronic mail!"
connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=msg_body)
connection.close()
