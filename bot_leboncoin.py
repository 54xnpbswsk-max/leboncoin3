import time
import requests
import feedparser
import os

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# lien RSS avec tes critères
RSS_URL = "https://www.leboncoin.fr/recherche?category=2&price=min-2000&mileage=min-200000&u_car_brand=AUDI,BMW,CITROEN,FORD,OPEL,PEUGEOT,RENAULT,VOLKSWAGEN,ALFA%20ROMEO,HONDA,HYUNDAI,KIA,NISSAN,TOYOTA&u_car_model=AUDI_A3,BMW_S%C3%A9rie%201,CITROEN_C1,CITROEN_C2,CITROEN_C3,OPEL_Corsa,PEUGEOT_107,PEUGEOT_207,PEUGEOT_206,PEUGEOT_307,PEUGEOT_306,PEUGEOT_308,RENAULT_Clio,RENAULT_Megane,RENAULT_Twingo,VOLKSWAGEN_Golf,VOLKSWAGEN_Polo&sort=time&order=desc&rss=true"

seen = set()

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": msg
    }
    requests.post(url, data=data)

while True:
    try:
        feed = feedparser.parse(RSS_URL)

        for entry in feed.entries:
            link = entry.link

            if link not in seen:
                seen.add(link)

                message = f"🚗 Nouvelle annonce :\n{entry.title}\n{link}"
                send_telegram(message)

        time.sleep(60)

    except Exception as e:
        print("Erreur :", e)
        time.sleep(60)
