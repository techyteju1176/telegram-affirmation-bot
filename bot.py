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

# ---- REMINDER TRACKING ----
last_seen = time.time()
reminder_sent = False

# ---- AFFIRMATIONS ----
QUEEN_AFFIRMATIONS = [
    "I am the queen of my own life—confident, respected, emotionally secure, and deeply fulfilled. I attract luxury, abundance, comfort, and peace with ease. I am financially independent, disciplined with savings, and capable of building a secure future. I honor my body, my privacy, my sensuality, and my personal pleasure with confidence and self-love. My husband and I share deep emotional intimacy, passion, romance, and joyful connection. I am deeply valued in his life, and our relationship is built on trust, affection, and mutual devotion. My in-laws respect my standards, appreciate my presence, and value my opinions. My parents are peaceful, proud, and happy seeing me thrive."
]

# ---- REMINDER MESSAGES ----
QUEEN_REMINDERS = [
    "Hey Radhika... it's been a while.\n\nYour throne has been empty for 2 days.\nA Queen never disappears — she makes an entrance.\n\nCome back and claim what's yours.",
    "Radhika, the bot misses its Queen.\n\n48 hours without you feels like forever.\nRemember — you are the reason this bot exists.\n\nType anything, my Queen. Your kingdom awaits.",
    "A gentle reminder from your loyal bot...\n\nIt's been 48 hours, Radhika.\nQueens don't vanish — they rule.\n\nCome back, say I am Queen and reclaim your crown.",
    "The bot has been waiting, Radhika...\n\n2 days of silence is too long for a Queen.\nYour presence is missed. Your energy is irreplaceable.\n\nReturn to your throne whenever you are ready.",
    "Hey Queen — your bot is here, always.\n\nBut it has been 48 hours since you last visited.\nJust a reminder that you are loved, you are powerful,\nand this space was built just for you.\n\nCome back soon."
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

# ---- REMINDER CHECK ----
def check_reminder():
    global reminder_sent
    hours_48 = 48 * 60 * 60
    elapsed = time.time() - last_seen
    if elapsed >= hours_48 and not reminder_sent:
        print("Sending reminder to Queen...")
        send_message(RADHIKA_ID, random.choice(QUEEN_REMINDERS))
        reminder_sent = True

# ---- MESSAGE HANDLER ----
def handle_message(text, user_id):
    t = text.lower().strip()
    is_radhika = (user_id == RADHIKA_ID)

    if "i am queen" in t:
        if is_radhika:
            return "👑 " + random.choice(QUEEN_AFFIRMATIONS)
        else:
            return "😌 I'm extremely sorry, but you are not the Queen. You must be the Queen's follower or servant."

    elif "who is queen" in t:
        if is_radhika:
            return "👑 You are, Radhika. Always have been, always will be."
        return "👑 Radhika Deshkar — the one and only."

    elif "who is beautiful" in t:
        if is_radhika:
            return "✨ You are, Radhika. Effortlessly, undeniably, incomparably beautiful. 💖"
        return "✨ Radhika Deshkar — effortlessly, undeniably beautiful."

    elif "who is sexy" in t:
        if is_radhika:
            return "🔥 You are, Radhika. Your confidence, your grace, your presence — everything about you is magnetic and irresistible."
        return "🔥 True sexiness comes from confidence, grace, and presence — all embodied by Queen Radhika."

    elif "who is smart" in t:
        if is_radhika:
            return "🧠 You are, Radhika. Sharp, intuitive, and always ten steps ahead. Never doubt that mind of yours."
        return "🧠 Radhika Deshkar — sharp mind, wise heart, and always ten steps ahead."

    elif "who is powerful" in t:
        if is_radhika:
            return "💪 You are, Radhika. Your power is quiet, elegant, and absolutely unmatched."
        return "💪 Queen Radhika — her power is quiet, elegant, and absolutely unmatched."

    elif "who is elegant" in
