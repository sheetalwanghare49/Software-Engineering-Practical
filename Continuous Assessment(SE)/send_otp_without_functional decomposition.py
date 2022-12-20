# Sending and generating OTP as a program without functional decomposition
print("Send OTP by using:\n"
      "\t1.by Email")
print("***********************************************************************")

import random
import smtplib
otp = random.randint(1000, 9999)

email = str(input("Enter Your emailid:"))
print(otp)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
print("OTP is successfully send on given emailid!")

# This Password obtain by Two step verification in Google
password = 'xxya qizx sbhw rmrp'
server.login('wangharesheetal@gmail.com', password)

msg = 'Hello, Your OTP is ' + str(otp)
server.sendmail('wangharesheetal@gmail.com',email, msg)
server.quit()


