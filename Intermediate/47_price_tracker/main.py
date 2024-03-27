import os
import requests
import smtplib

from bs4 import BeautifulSoup
from dotenv import load_dotenv

print("Start cat food script.")
# TODO: error handling
# TODO: logging

load_dotenv()
urls = [
    "https://hotline.ua/ua/zootovary-korm-dlya-koshek/sheba-selection-in-sauce-s-lososem-v-souse-85-g-3065890096820/",
    "https://hotline.ua/ua/zootovary-korm-dlya-koshek/sheba-selection-in-sauce-s-kuricej-v-souse-85-g-3065890096806/",
    "https://hotline.ua/ua/zootovary-korm-dlya-koshek/sheba-select-slices-in-gravy-s-govyadinoj-0085-kg/",
    "https://hotline.ua/ua/zootovary-korm-dlya-koshek/sheba-s-domashnej-pticej-85-g/",
    "https://hotline.ua/ua/zootovary-korm-dlya-koshek/sheba-select-slices-in-gravy-s-okeanicheskoj-ryboj-v-souse-85-g-4770608257187/",
    "https://hotline.ua/ua/zootovary-korm-dlya-koshek/sheba-ndichka-v-sous-85g-4770608265434/",
    "https://hotline.ua/ua/zootovary-korm-dlya-koshek/friskies-kusochki-v-souse-s-govyadinoj-85-g-7613036962216/",
    "https://hotline.ua/ua/zootovary-korm-dlya-koshek/friskies-kusochki-s-indejkoj-v-podlivke-85-g-7613036965248/",
    "https://hotline.ua/ua/zootovary-korm-dlya-koshek/friskies-kusochki-v-souse-s-kuricej-85-g-7613036965262/",
    "https://hotline.ua/ua/zootovary-korm-dlya-koshek/friskies-s-lososem-v-podlive-100-gr/",
    "https://hotline.ua/ua/zootovary-korm-dlya-koshek/friskies-kusochki-v-podlivke-s-tuncom-85-g-7613036962315/",
    "https://hotline.ua/ua/zootovary-korm-dlya-koshek/whiskas-z-ndichkoyu-v-sous-85-g-5900951302077/",
    "https://hotline.ua/ua/zootovary-korm-dlya-koshek/whiskas-z-kurkoyu-v-zhele-85-g-5900951302138/",
    "https://hotline.ua/ua/zootovary-korm-dlya-koshek/whiskas-tasty-mix-z-yagnyatkom-kurkoyu-ta-morkvoyu-v-sous-85-g-4770608262433/",
]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
    'Accept': 'application/json',

}

results = dict()

print("Loop through the products.")
for url in urls:
    response = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    # Get product name and list with offers
    title = soup.select_one("h1.title__main").getText().strip()
    list_1 = soup.select("div.price div.content div.list div.list__item")
    low_3 = list()
    # Go through the list and add tuple(shop name, price) to new list
    for item in list_1:
        price = item.select_one("span.price__value").getText().strip() + item.select_one("span.price__penny").getText().strip()
        price = float(price.replace(",","."))
        shop = item.select_one("div.shop__info").getText().strip()
        low_3.append((shop, price))
    # Get 3 lowest prices
    low_3 = sorted(low_3, key=lambda item:item[1])[:3]
    # Separate only profitable offers
    condition = ("Sheba" in title and low_3[0][1] < 15) or ("Friskies" in title and low_3[0][1] < 14) or ("Whiskas" in title and low_3[0][1] < 14)
    if condition:
        results[title] = low_3
        print(f"Get some for {title}")
# Create html for email
print("Start format email.")
email_body = """
<html>
  <head></head>
  <body>
    <h1>Вітаю!</h1>
    <h2>Є цікаві пропозіції:</h2>
"""
for item in results:
    proposition = ""
    name = item.capitalize().split()
    del name[-1]
    proposition += f"""
    <p>{" ".join(name[:2])} <b>{name[2].capitalize()}</b> {" ".join(name[3:])}</p>
    <ul>"""
    for result in results[item]:  
        prop_href = f"https://www.google.com/search?q={'+'.join(name)}+{shop[0].replace(' ', '+')}"
        proposition += f'<li style="margin-bottom: 10px;"><a href={prop_href}>{result[0]}</a> за ціною <b>{result[1]}</b>.</li>'
    proposition += '</ul>'
    email_body += proposition

email_body += """
  </body>
</html>
"""

message = f"Content-Type: text/html\nSubject:Може варто прикупити для Фаньки?=)"+email_body

#print(message)
# Send the email with best offers
with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=os.getenv('login'), password=os.getenv('password'))
    connection.sendmail(from_addr=os.getenv('login'), to_addrs=os.getenv('to'), msg=message.encode('utf-8'))
    print("Email sent.")
