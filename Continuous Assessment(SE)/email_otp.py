import random
import smtplib
otp = random.randint(1000, 9999)
server = smtplib.SMTP('smtp.gmail.com', 587)
print(server)
server.starttls()
#This Password obtain by Two step verification in Google
password= 'xxya qizx sbhw rmrp'
server.login('wangharesheetal@gmail.com',password)
msg='Hello, Your OTP is '+str(otp)
a=str(input("Enter Your emailid:"))
server.sendmail('wangharesheetal@gmail.com',a ,msg)
server.quit()


