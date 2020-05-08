from bs4 import BeautifulSoup
import requests
import smtplib
import time
import tkinter
from tkinter import *
from twilio.rest import Client

main = Tk()

main.title("Best Deals")
main.configure(bg='grey')
main.geometry("600x400")

label1=Label(main, text="Link",font=("montserrat",15), fg="black").place(x=50,y=20)
label2=Label(main, text="Price",font=("montserrat",15), fg="black").place(x=50,y=60)

link= StringVar()
price_my=DoubleVar()
entry1=Entry(main,textvariable = link,width='26').place(x=120,y=20)
entry2=Entry(main,textvariable = price_my,width='26').place(x=120,y=60)

def doit():
    if(link.get() == ""):
        print("Please Enter data in all field")
    else:
        print(link.get())
        print("You may now close the window")

but=Button(main,text="Enter",command=doit).place(x=140,y=95)
main.mainloop()

URL=link.get()
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
hg = soup.find("h1", class_="pcstname").get_text()#as per html code
print("Stock Name- "+ hg)

e=(price_my.get())  

def checkprice():
    price = soup.find("div", class_="pcnsb div_live_price_wrap").get_text()#as per html code
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
    week = soup.find("h1", class_="pcstname").get_text()#as per html code
    server.login('from@gmail.com' , 'phone_no')
    subject= week + ' Price fell down'
    print(subject)
    body= 'Anything '
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail( 'from@gmail.com', 'to@gmail.com',msg)
    my_cell = "+91"
    my_twilio = ""#open twilio account
    account_sid = ""#given in twilio account
    auth_token  = ""#given in twilio account
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    to=my_cell,
    from_=my_twilio,
    body=subject)

    print('SENTTTTTTT')
    server.quit()

while(TRUE):
    print()
    checkprice()
    time.sleep(10)