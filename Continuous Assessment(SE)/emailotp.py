import random
import re
import smtplib

# Method of Generation of otp

otp_length = random.randint(4,7)
def generate_otp(otp_length):
    otp = ''
    for i in range(otp_length):
        value = random.randint(0,9)
        otp = otp +str(value)

    return otp


# Method of Validation of email


def validate_email(email):
    p = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    if(re.search(p,email)):
        print("Given Email is valid.")

        return True
    else:
        raise AssertionError(email+' is not valid email id!')


def otp_length(otp):
    if not (4<=len(otp) and len(otp)>=8):
        raise AssertionError("Length of otp should be in between 4 to 8")
    else:
        print("Length of otp is valid!")


# Method of Sending otp

def send_otp(mailid,otp):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    password = 'xxya qizx sbhw rmrp'
    sender_mail = "wangharesheetal@gmail.com"
    otp = generate_otp(otp_length)
    msg = 'Hello, Your OTP is ' + str(otp)
    server.login(sender_mail,password)
    server.sendmail("wangharesheetal@gmail.com",mailid,msg)
    server.quit()
    print("OTP send !!")









