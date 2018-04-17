from share_prj.settings import SENDER_EMAIL, SENDER_PASSWORD
import smtplib


def my_send_mail(name, email, number, text):

    msg = """
        Hello, You have a new contact request from """ + name + """
         
        Name: """ + name + """       
        Email: """ + email + """
        Number: """ + number + """
        Message: """ + text + """
    """
    msg.format(name, email, number, text)

    email_msg = "Subject: Contact Request \n\n" + msg.format()
    smtp = smtplib.SMTP('smtp.gmail.com')
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
    recipiant = SENDER_EMAIL



    smtp.sendmail(SENDER_EMAIL, recipiant, email_msg)

    smtp.quit()

