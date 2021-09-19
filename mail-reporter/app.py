from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage 
from email import encoders
from smtplib import SMTP
from datetime import datetime
import config
from time import sleep


def main():
    #Create message object instance
    msg = MIMEMultipart()

    #Message to send
    message = 'А это уже второе сообщение, которое не требует проверки.' 

    #Settings import
    msg['From'] = config.My_Email
    msg['To'] = config.To_Email
    msg['Subject'] = 'Testing Message'
     
    #Calculate date for name file
    prefix_name_file = datetime.now().strftime(r'%d')
    prefix_name_file = str(int(prefix_name_file) - config.Day_before)

    #Add in the message body
    msg.attach(MIMEText(message, 'plain'))

    #Format name for send file
    file_name = './res/{}_file.txt'.format(prefix_name_file) # file_name пока что не используется, на время теста.

    #Add FILE in the message
    #Create Parting
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open('./res/file.txt', 'rb').read()) #Для теста - имя абсолютное, в релизе используется file_name
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="file.txt"') #Здесь так же пока что имя - абсолютное
    msg.attach(part)

    #Create server
    #server = SMTP(host='smtp.mail.ru', port=587)
    with SMTP('smtp.mail.ru: 587') as smtp:
        smtp.set_debuglevel(True)

        smtp.starttls()

        #Create login
        smtp.login(config.My_Email, config.My_Password_Email)

        #Send the message via the server
        smtp.sendmail(config.My_Email, config.To_Email, msg.as_string())

        smtp.quit()

        print('Successfully send!')


main() 


''' Закоментировал для теста. В релизе должна быть проверка каждый час в соответствии
    с указанным часом отправки(в config.py)

'''

'''
while True:
    if datetime.now().strftime(r'%H') == config.time_send:
        main()
    else:
        sleep(3600)
'''