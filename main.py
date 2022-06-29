import smtplib
import requests
from bs4 import BeautifulSoup

MY_EMAIL = MY_EMAIL
MY_PASSWORD = MY_PASSWORD
AMAZON_URL = "https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/" \
             "ref=dp_fod_2?pd_rd_i=B01NBKTPTS&psc=1"

headers = {
    "User-Agent": USER-AGENT
    "Accept-Language": ACCEPT LANGUAGE
}  #amazon is funky and they require these headers. You can find YOUR computer info here: http://myhttpheader.com/

response = requests.get(AMAZON_URL, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')

price_point = (soup.find("span", class_="a-price-whole").getText().split('.'))
price_float = int(price_point[0])
product_title = soup.find("span", id="productTitle").getText().strip().split("Plus")

if price_float < 100:
    message = f"{product_title[0]} is on sale! The price is currently: ${price_float}\n" \
              f"You can find the product at {AMAZON_URL}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Amazon Price Alert\n\n {message}\n "
            # I tried with the full message here, but wasn't working, I think that there is a limit.
        )

else:
    print(f"Sorry your price point is not low enough. It is currently ${price_float}")
