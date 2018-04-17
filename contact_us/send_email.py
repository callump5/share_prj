from share_prj.settings import SENDER_EMAIL, SENDER_PASSWORD
import smtplib


def my_send_mail(msg):
    smtp = smtplib.SMTP('smtp.gmail.com', 465)

    smtp.login(SENDER_EMAIL, SENDER_PASSWORD)

    recipiant = SENDER_EMAIL
    smtp.sendmail(SENDER_EMAIL, recipiant, msg)

    return