import requests
from bs4 import BeautifulSoup
import smtplib
import time




URL = 'https://www.amazon.in/Bose-Quiet-Comfort-Wireless-Headphone/dp/B0756CYWWD/ref=sr_1_3?crid=26KN2RKFQDNJG&dchild=1&keywords=bose+headphones&qid=1597234584&sprefix=bose+%2Caps%2C340&sr=8-3'


headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}



def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = price[0:8]

    if(converted_price < '20,000') :
        send_mail()
    

    print(converted_price)
    print(title.strip())

    if(converted_price < '20,000') :
        send_mail()
    

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('email','pass')

    subject = 'Price fell down !'
    body = 'Check the link https://www.amazon.in/dp/B07S26X16N/ref=cm_sw_r_cp_api_i_ROgdFbG3T0Y2K'



    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'from@gmail.com',
        'to@gmail.com',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()







while(True):
    check_price()
    time.sleep(3600)