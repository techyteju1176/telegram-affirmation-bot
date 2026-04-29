import os
import random
import time
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
URL = f"https://api.telegram.org/bot{TOKEN}"

# ---- USER CONFIG ----
OWNER_ID = 5614161691
RADHIKA_ID = 1406577493

# ---- AFFIRMATIONS ----
QUEEN_AFFIRMATIONS = [
"I am the queen of my own life—confident, respected, emotionally secure, and deeply fulfilled. I attract luxury, abundance, comfort, and peace with ease. I am financially independent, disciplined with savings, and capable of building a secure future. I honor my body, my privacy, my sensuality, and my personal pleasure with confidence and self-love. My husband and I share deep emotional intimacy, passion, romance, and joyful connection. I am deeply valued in his life, and our relationship is built on trust, affection, and mutual devotion. My in-laws respect my standards, appreciate my presence, and value my opinions. My parents are peaceful, proud, and happy seeing me thrive."]

# ---- TELEGRAM FUNCTIONS ----

def get_updates(offset=None):
    url = URL + "/getUpdates"
    params = {"timeout": 30, "offset": offset}

    try:
        response = requests.get(url, params=params, timeout=35)
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Network issue:", e)
        time.sleep(5)
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
        print("SEND STATUS:", res.status_code)

    except Exception as e:
        print("Error sending message:", e)


# ---- MESSAGE HANDLER ----

def handle_message(text, user_id):
    text = text.lower().strip()

    # ---- I AM QUEEN ----
    if "i am queen" in text:
        if user_id == RADHIKA_ID:
            return "👑 " + random.choice(QUEEN_AFFIRMATIONS)

        else:
            return "😌 I'm extremely sorry, but you are not the Queen. You must be the Queen's follower or servant."

    # ---- WHO IS QUEEN ----
    elif "who is queen" in text:
        return "👑 Radhika Deshkar"

    # ---- WHO IS BEAUTIFUL ----
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

            user = msg.get("from", {})
            user_id = user.get("id")
            name = user.get("first_name")

            print(f"USER ID: {user_id} | NAME: {name} | TEXT: {text}")

            if not text:
                continue

            reply = handle_message(text, user_id)

            print("REPLY:", reply)

            if reply:
                send_message(chat_id, reply)

        time.sleep(1)


# ---- START ----

if __name__ == "__main__":
    main()
