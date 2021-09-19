from smtplib import SMTP
import config

with SMTP('smtp.mail.ru: 587') as smtp:
    print(smtp.noop())
    smtp.starttls()
    smtp.set_debuglevel(True)
    smtp.login(config.My_Email, config.My_Password_Email)

    smtp.sendmail(config.My_Email, config.To_Email, 'Hello!')

    smtp.quit()

 