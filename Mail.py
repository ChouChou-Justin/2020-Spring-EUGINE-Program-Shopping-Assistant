import smtplib
import RegularExpression as RE
from email.mime.text import MIMEText

def EnterRecipient():
    mail = RE.DetectMail(mail=input("Type in your Email address: "))
    blank = [[]]
    if mail in blank:
        print("The type of your Email address might be wrong or blanks!")
        EnterRecipient()
    else:
        emailAddress = mail[0]
        print("Your Email address is {}".format(emailAddress))

    return emailAddress

def SendMail(productName, productPrice, latestPrice, mail):
    gmail_user = 'justin0010523@gmail.com'
    key = 'ofregavbnnsyavom'

    if productPrice < latestPrice:
        msg = MIMEText("The price of {} in Amazon has decreased! Buy it now!".format(productName))
    elif productPrice > latestPrice:
        msg = MIMEText("The price of {} in Amazon has increased! What a shame!".format(productName))

    msg['Subject'] = 'Amazon price changed!'
    msg['From'] = gmail_user
    msg['To'] = mail

    smtpssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtpssl.ehlo()
    smtpssl.login(gmail_user, key)
    smtpssl.send_message(msg)
    smtpssl.quit()

    return print('Email has been sent!')
