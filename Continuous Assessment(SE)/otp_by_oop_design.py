#implementation of OTP Assignment as per OOP design
import random
import re
import smtplib

class sendotp:
    #constructor
    def __init__(self,email,length):
        self.email = email
        self.length = length
        self.validate_email()
        x = self.generate_otp()
        self.send_otp(x)

    # Method of Generation of otp
    otp_length = random.randint(4, 7)
    def generate_otp(self):
        otp = ''
        for i in range(otp_length):
            value = random.randint(0, 9)

            otp = otp + str(value)
        return otp


    # Method of Validation of email
    def validate_email(email):
        p = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        if (re.search(p, email)):
            print("Given Email is valid.")

            return True
        else:
            print("Given Email is not valid!")

            return False

        # Method of Sending otp

        def send_otp(self,otp):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            password = 'xxya qizx sbhw rmrp'
            sender_mail = "wangharesheetal@gmail.com"
            self.otp = otp
            msg = 'Hello, Your OTP is ' + str(otp)
            server.login(sender_mail, password)
            server.sendmail("wangharesheetal@gmail.com", mailid, msg)
            server.quit()
            print("OTP send !!")


length = random.randint(4,7)
program1 = sendotp("sheetalwanghare123@gmail.com",length)
