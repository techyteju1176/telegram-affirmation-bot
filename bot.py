import os
import random
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
URL = f"https://api.telegram.org/bot{TOKEN}"

QUEEN_AFFIRMATIONS = [
    "Yes Radhika You are a Queen, Now Take Out Sometime Amd choose something powerful which i'll send you whenever You say the truth I AM QUEEN"]


def get_updates(offset=None):
    url = URL + "/getUpdates"
    params = {"timeout": 30, "offset": offset}
    response = requests.get(url, params=params)
    return response.json()


def send_message(chat_id, text):
    url = URL + "/sendMessage"
    requests.post(url, json={
        "chat_id": chat_id,
        "text": text
    })

 
def handle_message(text):
    text = text.lower().strip()

    if "i am queen" in text:
        return "👑 " + random.choice(QUEEN_AFFIRMATIONS)

    elif text == "who is queen on the earth":
        return "👑 Radhika Deshkar"

    elif text == "who is beautiful ?" or text == "who is beautiful":
        return "✨ Radhika Deshkar"

    return None


def main():
    offset = None

    while True:
        data = get_updates(offset)

        for item in data.get("result", []):
            offset = item["update_id"] + 1

            if "message" in item:
                msg = item["message"]
                chat_id = msg["chat"]["id"]
                text = msg.get("text", "")

                if not text:
                    continue

                reply = handle_message(text)

                if reply:
                    send_message(chat_id, reply)


if __name__ == "__main__":
    main()
