from new_settings.base import SENDER_EMAIL, SENDER_PASSWORD
import smtplib


def my_send_mail(name, email, number, text):

    msg = """
        Hello, You have a new contact request from """ + name + """
         
        Name: """ + name + """       
        Email: """ + email + """
        Number: """ + number + """
        Message: \n """ + text + """
    """
    msg.format(name, email, number, text)

    email_msg = "Subject: Contact Request \n\n" + msg.format()
    smtp = smtplib.SMTP('smtp.gmail.com')
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
    recipiant = 'share.enquiries@gmail.com'



    smtp.sendmail(SENDER_EMAIL, recipiant, email_msg)


    smtp.quit()


