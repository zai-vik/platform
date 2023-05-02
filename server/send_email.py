import smtplib
from email.mime.text import MIMEText
import base64

import os
from dotenv import load_dotenv

load_dotenv()



def send_email(email, code):

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(os.getenv('EMAIL'), os.getenv('PASSWORD'))

    with open('templates/email.html', 'r', encoding='UTF-8') as file:
        template = file.read()
        template = template.replace('VerifCode', code)

        with open('templates/email.png', 'rb') as image:
            binary_fc = image.read()
            image.close()
            base64_utf8_str = base64.b64encode(binary_fc).decode('utf-8')

        ext = 'templates/email.png'.split('.')[-1]
        dataurl = f'data:image/{ext};base64,{base64_utf8_str}'

        template = template.replace('PicSrc', dataurl)

    msg = MIMEText(template, 'html')

    msg['From'] = os.getenv('EMAIL')
    msg['To'] = email
    msg['Subject'] = 'Ваш код подтверждения'
    server.sendmail(os.getenv('EMAIL'), email, msg.as_string())
