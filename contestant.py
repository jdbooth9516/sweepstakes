from user_interface import User_interface
import smtplib
from socket import gaierror





class Contestant:
    def __init__(self, fname, lname, email, registration_number):
        self.first_name = fname
        self.last_name = lname
        self.email = email
        self.registration = registration_number
        self.ui = User_interface()
       

    def notify(self):
        self.ui.recieve_message(self.first_name)
        sender = "Contest Manager <from@contest.com>"
        receiver = f'{self.first_name} {self.last_name} <{self.email}>'
        message = f"""\
            subject: The winner has been selected
            To : {receiver}
            From: {sender}

            Sorry to inform you that you did not win. """
        
        try:
    #send your message with credentials specified above
            with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
                server.login("13bac95453bc7e", "a5d5ba65657bb7")
                server.sendmail(sender, receiver, message)

    # tell the script to report if your message was sent or which errors need to be fixed
            print('Sent')
        except (gaierror, ConnectionRefusedError):
            print('Failed to connect to the server. Bad connection settings?')
        except smtplib.SMTPServerDisconnected:
            print('Failed to connect to the server. Wrong user/password?')
        except smtplib.SMTPException as e:
            print('SMTP error occurred: ' + str(e))

    def notify_winner (self):
        self.ui.recieve_winner(self.first_name)
        sender = "Contest Manager <from@contest.com>"
        receiver = f'{self.first_name} {self.last_name} <{self.email}>'
        message = f"""\
            subject: The winner has been selected
            To : {receiver}
            From: {sender}

            Congradulations you have won. """
        
        try:
    #send your message with credentials specified above
            with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
                server.login("13bac95453bc7e", "a5d5ba65657bb7")
                server.sendmail(sender, receiver, message)

    # tell the script to report if your message was sent or which errors need to be fixed
            print('Sent')
        except (gaierror, ConnectionRefusedError):
            print('Failed to connect to the server. Bad connection settings?')
        except smtplib.SMTPServerDisconnected:
            print('Failed to connect to the server. Wrong user/password?')
        except smtplib.SMTPException as e:
            print('SMTP error occurred: ' + str(e))