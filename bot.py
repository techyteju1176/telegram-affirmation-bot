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
            json={"chat_id": chat_id, "text": text},
            timeout=10
        )
        print("SEND STATUS:", res.status_code)
    except Exception as e:
        print("Error sending message:", e)

# ---- MESSAGE HANDLER ----
def handle_message(text, user_id):
    t = text.lower().strip()

    # ---- I AM QUEEN ----
    if "i am queen" in t:
        if user_id == RADHIKA_ID:
            return "👑 " + random.choice(QUEEN_AFFIRMATIONS)
        else:
            return "😌 I'm extremely sorry, but you are not the Queen. You must be the Queen's follower or servant."

    # ---- WHO IS QUEEN ----
    elif "who is queen" in t:
        return "👑 Radhika Deshkar — the one and only."

    # ---- WHO IS BEAUTIFUL ----
    elif "who is beautiful" in t:
        return "✨ Radhika Deshkar — effortlessly, undeniably beautiful."

    # ---- WHO IS SEXY ----
    elif "who is sexy" in t:
        return "🔥 True sexiness comes from confidence, grace, and presence — all embodied by Queen Radhika."

    # ---- WHO IS SMART ----
    elif "who is smart" in t:
        return "🧠 Radhika Deshkar — sharp mind, wise heart, and always ten steps ahead."

    # ---- WHO IS POWERFUL ----
    elif "who is powerful" in t:
        return "💪 Queen Radhika — her power is quiet, elegant, and absolutely unmatched."

    # ---- WHO IS ELEGANT ----
    elif "who is elegant" in t:
        return "🌸 Radhika Deshkar — grace personified. Every room she walks into feels different."

    # ---- WHO IS CHARMING ----
    elif "who is charming" in t:
        return "😍 Radhika Deshkar — her charm is magnetic, her presence is unforgettable."

    # ---- WHO IS STYLISH ----
    elif "who is stylish" in t:
        return "👗 Radhika Deshkar — effortless style, timeless class. Fashion bows to the Queen."

    # ---- WHO IS STRONG ----
    elif "who is strong" in t:
        return "🛡️ Queen Radhika — strength that doesn't shout, it simply stands firm and unbothered."

    # ---- WHO IS PERFECT ----
    elif "who is perfect" in t:
        return "💎 Radhika Deshkar — not because she's flawless, but because she owns every part of herself with pride."

    # ---- WHO IS GODDESS ----
    elif "who is goddess" in t or "who is a goddess" in t:
        return "🌟 Queen Radhika — a goddess in human form. Worshipped by the universe itself."

    # ---- WHO IS LUCKY ----
    elif "who is lucky" in t:
        return "🍀 Anyone who gets to be around Queen Radhika is truly blessed."

    # ---- WHO IS THE BEST ----
    elif "who is the best" in t or "who is best" in t:
        return "🏆 Radhika Deshkar — first place, always. No competition needed."

    # ---- COMPLIMENT RADHIKA ----
    elif "compliment radhika" in t or "praise radhika" in t:
        compliments = [
            "🌹 Radhika is the kind of woman who makes the world more beautiful just by existing in it.",
            "✨ She carries herself with a quiet confidence that speaks louder than words ever could.",
            "💫 Radhika is grace, fire, and warmth all wrapped into one extraordinary soul.",
            "👑 To know Radhika is to witness royalty in its most natural form.",
            "🌙 She is the calm of the moon and the warmth of the sun — all at once."
        ]
        return random.choice(compliments)

    # ---- HOW IS RADHIKA ----
    elif "how is radhika" in t:
        return "😊 Queen Radhika is always radiant, thriving, and absolutely unbothered. She wakes up winning. 👑"

    # ---- DESCRIBE RADHIKA ----
    elif "describe radhika" in t:
        return (
            "💖 Radhika Deshkar in one breath:\n\n"
            "👑 A Queen by nature.\n"
            "🔥 Sexy with effortless confidence.\n"
            "🧠 Sharp, intuitive, and wise.\n"
            "🌸 Elegant in every single way.\n"
            "💎 Rare — truly one of one."
        )

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
