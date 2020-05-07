from bs4 import BeautifulSoup
import requests
import smtplib
import time


URL="https://www.amazon.in/dp/B07XZHHMVV/ref=s9_acsd_ri_bw_r2_camerash_0_t?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-18&pf_rd_r=R7S2TBTS6GHX303DDZMK&pf_rd_t=101&pf_rd_p=2382b1e1-169e-4eb3-abc5-5be16cbe73d0&pf_rd_i=1375424031"
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}


def checkprice():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find(id = "mbc-price-1").get_text()
    need_price = float(price[2:4].strip()+price[5:9].strip())
    print(need_price)
    if(need_price < 140):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    week = soup.find("h1", class_="pcstname").get_text()
    server.login('addysarwankar@gmail.com' , '7208032334')
    subject= week + ' Price fell down'
    print(subject)
    body= 'Check link      https://www.moneycontrol.com/india/stockpricequote/finance-leasinghire-purchase/magmafincorp/MF20'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'addysarwankar@gmail.com',
        'adityasarwankar1999@gmail.com',
        msg
    )
    print('SENTTTTTTT')
    server.quit()

checkprice()



