from bs4 import BeautifulSoup
import requests
import smtplib
import time
import tkinter
import mysql.connector
from tkinter import *
from twilio.rest import Client

#mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234")
#print(mydb)
# if(mydb):
#     print("success")
# else:
#     print("unsuccess")

main = Tk()

main.title("ankit web")
main.configure(bg='black')
main.geometry("900x900")

label1=Label(main, text="Link",font=("montserrat",15), fg="black").place(x=50,y=20)
label2=Label(main, text="Price",font=("montserrat",15), fg="black").place(x=50,y=60)

link= StringVar()
price_my=DoubleVar()
entry1=Entry(main,textvariable = link,width='86').place(x=120,y=20)
entry2=Entry(main,textvariable = price_my,width='86').place(x=120,y=60)


#mycursor = mydb.cursor()
#sqlform = "Insert into customer(name,rupees) values(%link,%price)"

def doit():
    if(link.get() == ""):
        print("Please Enter data in all field")
    else:
        print(link.get())
        print("You may now close the window")

but=Button(main,text="Enter",command=doit).place(x=140,y=95)
main.mainloop()

URL=link.get()
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
#hg = soup.find('div', id="stockName")#print("Stock Name- "+ hg)

for heading in soup.find_all(["h1"]):
    print("Stock Name- "+heading.text.strip())

e=(price_my.get())  

def checkprice():
    price = soup.find("div", class_="inprice1 nsecp").get_text() #as per html code
    need_price = price.split(".")
    l=int(need_price[0])
    print("Current price:  ",l)
    print("Your expected price:  ",e)

    if(int(need_price[0]) < e ):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    week=""
    for heading in soup.find_all(["h1"]):
        week = heading.text.strip()
    server.login('sarwankarankan18it@student.mes.ac.in' , 'qgrhvngkaxqcxtiq')
    subject= week+ ' Price fell down [link:  '+URL+']'
    print(subject)
    body= 'Anything '
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail( 'sarwankarankan18it@student.mes.ac.in', 'ankitsarwankar@gmail.com',msg)
    my_cell = "+918928670213"
    my_twilio = "+13084705044"#open twilio account
    account_sid = "AC249ba1227b2c7ee9df6dbb1d5a37e172"#given in twilio account
    auth_token  = "9a9dcfaab92990917580e03ab407e7c1"#given in twilio account
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    to=my_cell,
    from_=my_twilio,
    body=subject)

    print('MESSAGE SENTTTT')
    server.quit()
#    mycursor.execute(sqlform)

#mydb.commit()

while(TRUE):
    print()
    checkprice()
    time.sleep(10)
