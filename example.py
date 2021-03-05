# import csv
# import smtplib
# import config
#
# # with open('myFile.csv', 'r') as csv_file:
# #     csv_reader = csv.reader(csv_file)
# #
# #     # print(csv_reader)
# #     for line in csv_reader:
# #         print(line[2])
#
#
# def send_email(subject, msg):
#     try:
#         server = smtplib.SMTP('smtp.gmail.com:587')
#         server.ehlo()
#         server.starttls()
#         server.login(config.EMAIL_ADDRESS, config.PASSWORD)
#         message = 'Subject: {} \n\n {}'.format(subject, msg)
#         server.sendmail(config.EMAIL_ADDRESS, config.PASSWORD, message)
#         server.quit()
#         print("Success: Email send!")
#
#     except:
#         print("Emial Failed to send.")
#
#
# sub = "Test subject"
# msg = "Hello there, how are you today??"
#
# send_email(sub, msg)



import smtplib as s
import csv

with open('myFile.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        listOfAddress = line[2]

        server = s.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login('email', 'password')
        subject = "Test subject"
        to_email = listOfAddress[line]
        body = "Hello this is testing email??"
        message = 'To: {} \n\n Subject: {} \n\n {}'.format(to_email, subject, body)
        # print(listOfAddress)

        # # print(message)
        # # listOfAddress = ['pansaresarika9@gmail.com', 'pansaresarika98@gmail.com', 'pratiksha.minskole@gmail.com']

        # server.sendmail('sarika.minskole@gmail.com', listOfAddress, message)

print("Success: Email send!")
server.quit()



import smtplib as s
import csv

# with open('myFile.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#
#     for line in csv_reader:
#         listOfAddress = line[2]

server = s.SMTP('smtp.gmail.com:587')
server.starttls()
server.login('email', 'password')
subject = "Test subject"
listOfAddress = ['email']
to_email = listOfAddress
body = "Hello this "
message = 'To: {} \n\n Subject: {} \n\n {}'.format(to_email, subject, body)

        # print(listOfAddress)

        # # print(message)
        # # listOfAddress = ['pansaresarika9@gmail.com', 'pansaresarika98@gmail.com', 'pratiksha.minskole@gmail.com']

server.sendmail('email', listOfAddress, message)

print("Success: Email send!")
server.quit()






body = ''' Dear Sarika, 

                Thank you for your interest in joining the free demo session for "Cypress", we are pleased to invite you for this semo session on Sunday 20th September 2020 at 4 pm IST

                Please note you will receive the Free Seminar invitation details shortly. We have very exciting offers, please join to check it out!!!!

                In case you have any questions, please do not hesitate to contact us on contact@minskole.in.  

                Once again Thank you for your interest & Have a nice day!!

                Best Regards
                MinSkole Team
                +91-7841938548
                old text_ (1).jpg
                https://minskole.in'''





















