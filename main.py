import bs4
import urllib.request
import smtplib
import time 
prices_list =[]
def check_price():
    url='https://www.amazon.in/boAt-BassHeads-100-Headphones-Black/dp/B071Z8M4KX/ref=sr_1_1?dchild=1&qid=1625908580&refinements=p_15%3ABoat&s=electronics&sr=1-1'
    sauce = urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(sauce,"html.parser")
    price=soup.find(id="priceblock_ourprice").get_text()
    price=float(price.replace(",","").replace("₹",""))
    prices_list.append(price)
    return price 

def  send_email(message):
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("shutter1flutter@gmail.com","dustyfast")
    s.sendmail("shutter1flutter@gmail.com","mehul1gulati@gmail.com",message)
    s.quit()
   

def price_decrease_check(price_list):
    if price_list[-1]<price_list[-2]:
        return True
    else:
        return False 
count=1
while True:
    current_price=check_price()
    if count>1:
        boolean =price_decrease_check(prices_list)
        if boolean:
            drop=prices_list[-1]-prices_list[-2]
            message="The price has decreased by Rs {drop} please check the item"           
            send_email(message)
    time.sleep(42000)
    count+=1    