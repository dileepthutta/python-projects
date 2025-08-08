import requests
from bs4 import BeautifulSoup
import smtplib

import os
from dotenv import load_dotenv

#To load environment variables from .env file
load_dotenv()


#URl of the product.
URL = "https://amzn.in/d/hcX7Ey4"

#Headers
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}

#Sending a request to the website.
response = requests.get(
    url=URL,
    headers=header
)

# To view the data of the webpage.
webPageData = BeautifulSoup(response.content, "html.parser")

# To get the price of the product.
price = webPageData.find(name="span", class_="aok-offscreen").get_text()

# To split the data and get only the price.
item_price = price.split()[0]

# Remove the symbol.
price_value = float(item_price.replace("₹",""))

# TO get the details of the product tile.
title_details = webPageData.find(id="productTitle").get_text().split()
title = " ".join(title_details)

# Adds a condition
BUT_PRICE = 100

#Final message to be sent.
message = f"{title} is now at {price}"

# If price is less than 100 then we receive a mail.

if price_value<BUT_PRICE:
    message = f"{title} is now at {price_value}"

    with smtplib.SMTP(os.environ['SMTP_ADDRESS'], port=587) as connection:
        connection.starttls()
        connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["RECIPIENT_EMAIL"],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode('utf-8')
        )
        print("Email sent")
else:
    print("Email not sent")