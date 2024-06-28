# FIRST WAY

import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from']= 'SENDER_NAME'  #SENDER NAME
email['to']='RECEIVER_EMAIL' # RECEIVER EMAIL
email['subject'] = 'You won millon dollars' # SUBJECT OF EMAIL

email.set_content('i am python master')  # CONTENT OF EMAIL

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('SENDER_EMAIL','xxxx xxxx xxxx xxxx') #REPLACE PASSWORD WITH APP PASSWORD
    smtp.send_message(email)
    print('all good boss')

# NOTES == APP PASSWORD IS GOOGLE ACCOUNT FEATURE THAT USE FOR IMPLEMNTATING OLDER VERSIONS AND PROGRAMS TO OR LESS SECUR AUTHENTICATION FOR USECAS OF EMAIL


# ________________________________________________________________________

# SECOND WAY
# import yagmail
# import smtplib
# from email.message import EmailMessage

# # Email configuration
# email = EmailMessage()
# email['from'] = 'Divya Darji'
# email['to'] = 'divyadarji256@gmail.com'
# email['subject'] = 'You won a million dollars'

# email.set_content('I am a Python master')

# # SMTP server configuration
# smtp_server = 'smtp.gmail.com'
# smtp_port = 587
# username = 'thundergamerz403@gmail.com'
# password = 'euia tvpk ogjp pbau'  # Replace with the app password you generated

# try:
#     with smtplib.SMTP(host=smtp_server, port=smtp_port) as smtp:
#         smtp.ehlo()
#         smtp.starttls()
#         smtp.login(username, password)
#         smtp.send_message(email)
#         print('All good boss')
# except smtplib.SMTPAuthenticationError as e:
#     print(f'Failed to authenticate with SMTP server: {e}')
# except Exception as e:
#     print(f'An error occurred: {e}')



