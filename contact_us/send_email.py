from share_prj.settings import SENDER_EMAIL, SENDER_PASSWORD
import smtplib


def my_send_mail(msg):
    smtp = smtplib.SMTP('smtp.gmail.com')
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
    recipiant = SENDER_EMAIL

    smtp.sendmail(SENDER_EMAIL, recipiant, msg)

    smtp.quit()

