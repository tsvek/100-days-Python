import requests
import smtplib

# Separate .py file with login and password
from ap import login, password

def get_quote():
    url = "https://zenquotes.io/api/today"

    response = requests.get(url=url)
    data = response.json()[0]
    return data['q'], data['a']

quote = list(get_quote())
message = f"Subject:Quote for today\n\n{quote[0]}\n\n{quote[1]}\n\nHave a good day!!"

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=login, password=password)
    connection.sendmail(from_addr=login, to_addrs='tsvekt@outlook.com', msg=message)