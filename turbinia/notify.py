import logging
from turbinia import config

#Sends notfications via email
def sendmail(message):

    log=logging.getLogger('turbinia')
    try:
        EMAIL_NOTIFICATIONS = config.EMAIL_NOTIFCATIONS
        if EMAIL_NOTIFICATIONS == 'true':
            EMAIL_HOST_ADDRESS = config.EMAIL_HOST_ADDRESS
            EMAIL_PORT = int(config.EMAIL_PORT)

            EMAIL_ADDRESS = config.EMAIL_ADDRESS
            EMAIL_PASSWORD = config.EMAIL_PASSWORD

            RECIEVING_ADDRESS = config.RECIEVING_ADDRESS
            #Imports SMTP and  MIME(The format used for emails)
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            import smtplib

            #Puts message in MIME format
            msg = MIMEMultipart()
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = RECIEVING_ADDRESS
            msg['Subject'] = 'Notifcation from Turbina'
            msg.attach(MIMEText(message))

            #start SMTP
            server = smtplib.SMTP(EMAIL_HOST_ADDRESS,EMAIL_PORT)

            # identify to mail server
            server.ehlo()

            # secure email using TLS
            server.starttls()

            # reidentify and login to mail account
            server.ehlo()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            server.sendmail(EMAIL_ADDRESS, RECIEVING_ADDRESS,msg.as_string())

            #terminate connection
            server.quit()
            log.info('Email notification sent')
        else:
            log.info('Email notifications are disabled')
            pass
    except Exception as e:
            log.error(e)
            log.info('Email failed to send, check config')
            pass

def main(message):
    sendmail(message)
