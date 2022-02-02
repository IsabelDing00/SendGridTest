# -*- Coding = utf-8 -*-
# Author: Isabel Ding

from sendgrid import SendGridAPIClient
import os
from sendgrid.helpers.mail import *


API_KEY='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'


message = Mail(from_email='nate@bloom-mktg.info',
               to_emails='chongfanding@gmail.com',
               subject='Sending with SendGrid is Fun',
               plain_text_content='text/plain',
               html_content='<strong>and easy to do anywhere, even with Python</strong>',
               )
# sg = sendgrid.SendGridAPIClient(api_key=os.environ.get(API_KEY))
# from_email = Email("nate@bloom-mktg.info")  # Change to your verified sender
# to_email = To("chongfanding@gmail.com")  # Change to your recipient
# subject = "Sending with SendGrid is Fun"
# content = Content("text/plain", "and easy to do anywhere, even with Python")
# mail = Mail(from_email, to_email, subject, content)
#
# # Get a JSON-ready representation of the Mail object
# mail_json = mail.get()

# Send an HTTP POST request to /mail/send
try:
    sg = SendGridAPIClient(os.environ['SENDGRID_API_KEY'])
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)