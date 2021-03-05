import smtplib as s
import csv

with open('myFile3.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        name = line[0]
        listOfAddress = line[1]
        print(name)
        print(listOfAddress)

        server = s.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login('email', 'Password')

        subject = "Thank you for Registration"
        body = '''     msg body
        '''

        message = 'subject: {} \n\n Dear {}, \n\n {}'.format(subject, name, body)
        server.sendmail('email', listOfAddress, message)

print("Success: Email send!")
server.quit()
