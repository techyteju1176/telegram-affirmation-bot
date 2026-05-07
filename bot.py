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
    "I am the queen of my own life—confident, respected, emotionally secure, and deeply fulfilled. I attract luxury, abundance, comfort, and peace with ease. I am financially independent, disciplined with savings, and capable of building a secure future. I honor my body, my privacy, my sensuality, and my personal pleasure with confidence and self-love. My husband and I share deep emotional intimacy, passion, romance, and joyful connection. I am deeply valued in his life, and our relationship is built on trust, affection, and mutual devotion. My in-laws respect my standards, appreciate my presence, and value my opinions. My parents are peaceful, proud, and happy seeing me thrive."
]

# ---- TELEGRAM FUNCTIONS ----
def get_updates(offset=None):
    params = {"timeout": 30, "offset": offset}
    try:
        response = requests.get(URL + "/getUpdates", params=params, timeout=35)
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Network issue:", e)
        time.sleep(5)
        return {}

def send_message(chat_id, text):
    try:
        res = requests.post(
            URL + "/sendMessage",
            json={"chat_id": chat_id, "text": text},
            timeout=10
        )
        print("SEND STATUS:", res.status_code)
    except Exception as e:
        print("Error sending message:", e)

# ---- MESSAGE HANDLER ----
def handle_message(text, user_id):
    t = text.lower().strip()
    is_radhika = (user_id == RADHIKA_ID)

    # ---- I AM QUEEN ----
    if "i am queen" in t:
        if is_radhika:
            return "👑 " + random.choice(QUEEN_AFFIRMATIONS)
        else:
            return "😌 I'm extremely sorry, but you are not the Queen. You must be the Queen's follower or servant."

    # ---- WHO IS QUEEN ----
    elif "who is queen" in t:
        if is_radhika:
            return "👑 You are, Radhika. Always have been, always will be."
        return "👑 Radhika Deshkar — the one and only."

    # ---- WHO IS BEAUTIFUL ----
    elif "who is beautiful" in t:
        if is_radhika:
            return "✨ You are, Radhika. Effortlessly, undeniably, incomparably beautiful. 💖"
        return "✨ Radhika Deshkar — effortlessly, undeniably beautiful."

    # ---- WHO IS SEXY ----
    elif "who is sexy" in t:
        if is_radhika:
            return "🔥 You are, Radhika. Your confidence, your grace, your presence — everything about you is magnetic and irresistible."
        return "🔥 True sexiness comes from confidence, grace, and presence — all embodied by Queen Radhika."

    # ---- WHO IS SMART ----
    elif "who is smart" in t:
        if is_radhika:
            return "🧠 You are, Radhika. Sharp, intuitive, and always ten steps ahead. Never doubt that mind of yours."
        return "🧠 Radhika Deshkar — sharp mind, wise heart, and always ten steps ahead."

    # ---- WHO IS POWERFUL ----
    elif "who is powerful" in t:
        if is_radhika:
            return "💪 You are, Radhika. Your power is quiet, elegant, and absolutely unmatched."
        return "💪 Queen Radhika — her power is quiet, elegant, and absolutely unmatched."

    # ---- WHO IS ELEGANT ----
    elif "who is elegant" in t:
        if is_radhika:
            return "🌸 You are, Radhika. Grace personified. Every room you walk into feels warmer, more alive."
        return "🌸 Radhika Deshkar — grace personified. Every room she walks into feels different."

    # ---- WHO IS CHARMING ----
    elif "who is charming" in t:
        if is_radhika:
            return "😍 You are, Radhika. Your charm is magnetic and your presence is something people never forget."
        return "😍 Radhika Deshkar — her charm is magnetic, her presence is unforgettable."

    # ---- WHO IS STYLISH ----
    elif "who is stylish" in t:
        if is_radhika:
            return "👗 You are, Radhika. Effortless style, timeless class. Fashion doesn't define you — you define it."
        return "👗 Radhika Deshkar — effortless style, timeless class. Fashion bows to the Queen."

    # ---- WHO IS STRONG ----
    elif "who is strong" in t:
        if is_radhika:
            return "🛡️ You are, Radhika. Your strength doesn't shout — it stands firm, calm, and completely unbothered."
        return "🛡️ Queen Radhika — strength that doesn't shout, it simply stands firm and unbothered."

    # ---- WHO IS PERFECT ----
    elif "who is perfect" in t:
        if is_radhika:
            return "💎 You are, Radhika. You own every part of yourself with pride — and that is true perfection."
        return "💎 Radhika Deshkar — not because she's flawless, but because she owns every part of herself with pride."

    # ---- WHO IS GODDESS ----
    elif "who is goddess" in t or "who is a goddess" in t:
        if is_radhika:
            return "🌟 You are, Radhika. A goddess in human form. The universe itself bows to your energy."
        return "🌟 Queen Radhika — a goddess in human form. Worshipped by the universe itself."

    # ---- WHO IS LUCKY ----
    elif "who is lucky" in t:
        if is_radhika:
            return "🍀 Anyone who gets to be in your life, Radhika — they are truly, deeply blessed."
        return "🍀 Anyone who gets to be around Queen Radhika is truly blessed."

    # ---- WHO IS THE BEST ----
    elif "who is the best" in t or "who is best" in t:
        if is_radhika:
            return "🏆 You are, Radhika. First place, always. No competition, no comparison — just you."
        return "🏆 Radhika Deshkar — first place, always. No competition needed."

    # ---- COMPLIMENT RADHIKA ----
    elif "compliment radhika" in t or "praise radhika" in t:
        if is_radhika:
            return random.choice([
                "🌹 You make the world more beautiful just by existing in it, Radhika.",
                "✨ Your quiet confidence speaks louder than words ever could. Never lose it.",
                "💫 You are grace, fire, and warmth all wrapped into one extraordinary soul.",
                "👑 Being around you feels like being near royalty — because that's exactly what you are.",
                "🌙 You are the calm of the moon and the warmth of the sun — all at once, Radhika."
            ])
        return random.choice([
            "🌹 Radhika is the kind of woman who makes the world more beautiful just by existing in it.",
            "✨ She carries herself with a quiet confidence that speaks louder than words ever could.",
            "💫 Radhika is grace, fire, and warmth all wrapped into one extraordinary soul.",
            "👑 To know Radhika is to witness royalty in its most natural form.",
            "🌙 She is the calm of the moon and the warmth of the sun — all at once."
        ])

    # ---- HOW IS RADHIKA ----
    elif "how is radhika" in t:
        if is_radhika:
            return "😊 You tell me, my Queen — but I already know. You're radiant, thriving, and absolutely unbothered. You wake up winning. 👑"
        return "😊 Queen Radhika is always radiant, thriving, and absolutely unbothered. She wakes up winning. 👑"

    # ---- DESCRIBE RADHIKA ----
    elif "describe radhika" in t:
        if is_radhika:
            return (
                "💖 Let me tell you who you are, Radhika:\n\n"
                "👑 A Queen — by nature, not by title.\n"
                "🔥 Sexy with effortless, magnetic confidence.\n"
                "🧠 Sharp, intuitive, and beautifully wise.\n"
                "🌸 Elegant in every single way.\n"
                "💎 Rare — truly one of one.\n\n"
                "Don't ever forget it. 🌟"
            )
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
    print("✅ Bot is running...")
    while True:
        data = get_updates(offset)
        if "result" not in data:
            time.sleep(2)
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
