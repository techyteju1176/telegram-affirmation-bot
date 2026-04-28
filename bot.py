import os
import random
import time
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
URL = f"https://api.telegram.org/bot{TOKEN}"

# ---- AFFIRMATIONS ----
QUEEN_AFFIRMATIONS = [
    "Yes Radhika, you are a Queen. Take time and choose something powerful — I will remind you every time you say I AM QUEEN."
]

# ---- TELEGRAM FUNCTIONS ----

def get_updates(offset=None):
    try:
        url = URL + "/getUpdates"
        params = {"timeout": 30, "offset": offset}
        response = requests.get(url, params=params, timeout=35)
        return response.json()
    except Exception as e:
        print("Error fetching updates:", e)
        time.sleep(2)
        return {}


def send_message(chat_id, text):
    try:
        url = URL + "/sendMessage"
        res = requests.post(
            url,
            json={
                "chat_id": chat_id,
                "text": text
            },
            timeout=10
        )
        print("SEND STATUS:", res.status_code, res.text)

    except Exception as e:
        print("Error sending message:", e)


# ---- MESSAGE HANDLER ----

def handle_message(text):
    text = text.lower().strip()

    if "i am queen" in text:
        return "👑 " + random.choice(QUEEN_AFFIRMATIONS)

    elif "queen on the earth" in text:
        return "👑 Radhika Deshkar"

    elif "who is beautiful" in text:
        return "✨ Radhika Deshkar"

    return None


# ---- MAIN LOOP ----

def main():
    offset = None
    print("Bot is running...")

    while True:
        data = get_updates(offset)

        if "result" not in data:
            continue

        for item in data["result"]:
            offset = item["update_id"] + 1

            if "message" not in item:
                continue

            msg = item["message"]
            chat_id = msg["chat"]["id"]
            text = msg.get("text")

            # ---- USER LOGGING ----
            user = msg.get("from", {})
            user_id = user.get("id")
            name = user.get("first_name")

            print(f"USER ID: {user_id} | NAME: {name} | TEXT: {text}")

            if not text:
                continue

            reply = handle_message(text)

            print("REPLY:", reply)

            if reply:
                send_message(chat_id, reply)

        time.sleep(1)


# ---- START ----

if __name__ == "__main__":
    main()
