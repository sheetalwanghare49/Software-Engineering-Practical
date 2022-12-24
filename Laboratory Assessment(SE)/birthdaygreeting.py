#implement atleast three features for birthday greeting server application

import datetime
import imghdr
import mysql.connector
import os
import pywhatkit
import smtplib
from email.message import EmailMessage

#todays date
from swap_two_variables import x

now = str(datetime.date.today())
today = now[8:10]+now[5:7]
#print(now)

#database connection
mydb = mysql.connector.connect(host="localhost", user="root", passwd="sheetal@9702")
mycursor = mydb.cursor()

#insertion of data in database
def insertdata():
    insert = mydb.cursor()
    print("Enter details: ")
    name = input("Enter Name: ")
    bdate = input("Enter birthdate: ")
    email = input("Enter email: ")
    mobno = input("Enter mobile no: ")
    sql = "INSERT INTO bday_info(name,bdate,email,mobno) VALUES (%s, %s, %s, %s)"
    person = (name,bdate,email,mobno)
    insert.execute(sql,person)
    mydb.commit()

#display of data
def displaydata():
    display = mydb.cursor()
    display.execute("select * from data")
    data = display.fetchall()
    for i in data:
        print(i)

#sending whatsapp message
def sendmsg(info):
    name = info[0]
    mobno = '+91' + info[3]
    img = "https://in.images.search.yahoo.com/yhs/search;_ylt=AwrKEt60gaJj0C0E0nwO9olQ;_ylu=c2VjA3NlYXJjaARzbGsDYnV0dG9u;_ylc=X1MDMTM1MTIxODcwMgRfcgMyBGZyA3locy1Ma3J5LW50BGZyMgNwOnMsdjppLG06c2ItdG9wBGdwcmlkA3owLlNVb21sUUJhZGtFN2l3NDQ5ekEEbl9yc2x0AzAEbl9zdWdnAzMEb3JpZ2luA2luLmltYWdlcy5zZWFyY2gueWFob28uY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDMARxc3RybAMzMQRxdWVyeQNoYXBweSUyMGJpcnRoZGF5JTIwJTIwZ3JlZXRpbmdzaW1hZ2VzBHRfc3RtcAMxNjcxNTk0NDQ1?p=happy+birthday++greetingsimages&fr=yhs-Lkry-nt&fr2=p%3As%2Cv%3Ai%2Cm%3Asb-top&ei=UTF-8&x=wrt&type=YHS_STSRC4_58160_%2458160_001323%24&hsimp=yhs-nt&hspart=Lkry&param1=mT_KejuvTqqXvl656HwOKvu7_Yibdqwuj5xN9VhhLJ8fjMWedGO_aJh_lqgyhYzhFaw7pG9QV5CEHXa7K_kZqt1Cfua16HCQ639J68L95EsJWVwKMVVw7COyT5Dl937EDgR3ZSXGlx_B8hS9gJW3fGMCIdJEIj_0tze-v3JVBbyW9YDj5E_rlwGKmjL7_nkGjKcUVkyzbIdUsrW3WX5tcua2hPAb-mdt1q7jTPwLzwAUQBDBZS4Ny5p4pXRvn-qqOsExVFdN_EyNcWDFZR9cyRhtfjrA9KzFYvQ5FPojE3cXCqYoOa2swqlToIWoLyXgn4GojblQ9C8DymPhNx2VPNwHkLI9XayEztJll2e5QqWb5QIaEcNEjFzeuBGjYjDny0aBHJ1hYo9ZSdDSL64%2C#id=100&iurl=https%3A%2F%2Fhappybirthdaywishesfriend.com%2Fwp-content%2Fuploads%2F2021%2F05%2FReligious-Happy-Birthday-Wishes-for-a-Friend.jpg&action=click"
    pywhatkit.sendwhats_image(mobno,img,"Hello " +name+ "Wish you many many Happy returns of the day! Happy Birthday!",15,True,3)


def send_emailimage(info):
    with open("bdayimg.jpg", 'rb') as x:
        fdata= x.read()
        ftype = imghdr.what(x.name)
        fname = x.name

    password = 'xxya qizx sbhw rmrp'
    sendermail = "wangharesheetal@gmail.com"
    receivermail = bday_info[2]
    msg = EmailMessage()
    msg['Subject'] = "Sending Birthday Greetings!"
    msg['From'] = sendermail
    msg['to'] = receivermail
    msg.set_content("Hello " + data[0] + "\nWish you many many Happy returns of the day! Happy Birthday!!")
    msg.add_attachment(fdata,maintype = 'image',subtype = ftype, filename = fname)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sendermail,password)
    server.send_message(msg)
    print("msg send!")
    server.quit()

def send_emailtext():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    password = 'xxya qizx sbhw rmrp'
    sendermail = "wangharesheetal@gmail.com"
    receivermail = bday_info[2]
    msg = "Hello " + data[0] + "\nWish you many many Happy returns of the day! Happy Birthday!!"
    server.login(sendermail, password)
    server.sendmail("wangharesheetal@gmail.com", email, msg)
    print("email is send!!")
    server.quit()


insertdata()
displaydata()
mycursor.execute(f"select * from data where bdate = {today}")
list1 = mycursor.fetchall()
for i in list1:
    send_emailimage(i)
    sendmsg(i)
    send_emailtext(i)