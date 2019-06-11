import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def mailer(result,to):
    

    me = "ComboApp"
    you = to

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "ComboFinder"
    msg['From'] = me
    msg['To'] = you

    # Create the body of the message (a plain-text and an HTML version).
    text = "ComboFinder:\nHere are your best Combinations\n"+str(result).replace('\'','')
    part1 = MIMEText(text, 'plain')

    msg.attach(part1)


    s = smtplib.SMTP('smtp.gmail.com',587)

    s.ehlo()
    s.starttls()
    s.login('your@gmail.com','yourpassword') #makesure to enable third party app access on in your google account
											 # https://myaccount.google.com/lesssecureapps	<-- visit this link					
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.sendmail(me, you, msg.as_string())
    s.quit()