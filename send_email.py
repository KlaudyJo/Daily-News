from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL ='email'
MY_PASSWORD = 'password'
emails = ['email']

class EmailSent:
    
    def send_email(self,text,stocks_table, crypto_table, news):
        for email in emails:
            message = MIMEMultipart('alternative')
            message['Subject'] = 'News!'
            message['From'] =  MY_EMAIL
            message['To'] = email
            html = ''
            html += f'<h3>{text}</h3>'
            for article in news:
                html += f'<h4>{article}</h4>'
            html += stocks_table.to_html(index=False, classes='table table-striped text-center', justify='center')
            html += '<br>'
            html += crypto_table.to_html(index=False,classes='table table-striped text-center', justify='center')
            
            part2= MIMEText(html.encode('utf-8'),'html','utf-8')
            message.attach(part2)
            server = SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(message['From'], MY_PASSWORD)
            server.sendmail(message['From'], message['To'], message.as_string())
            server.quit()

