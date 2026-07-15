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

# ---- FILE TO SAVE LAST SEEN ----
LAST_SEEN_FILE = "last_seen.txt"

# ---- REMINDER MESSAGES ----
QUEEN_REMINDERS = [
    "Hey Radhika... it's been a while.\n\nYour throne has been empty for 2 days.\nA Queen never disappears — she makes an entrance.\n\nCome back and claim what's yours. 👑",
    "Radhika, the bot misses its Queen.\n\n48 hours without you feels like forever.\nRemember — you are the reason this bot exists.\n\nType anything, my Queen. Your kingdom awaits. 👑",
    "A gentle reminder from your loyal bot...\n\nIt's been 48 hours, Radhika.\nQueens don't vanish — they rule.\n\nCome back, say I am Queen and reclaim your crown. 👑",
    "The bot has been waiting, Radhika...\n\n2 days of silence is too long for a Queen.\nYour presence is missed. Your energy is irreplaceable.\n\nReturn to your throne whenever you are ready. 👑",
    "Hey Queen — your bot is here, always.\n\nBut it has been 48 hours since you last visited.\nJust a reminder that you are loved, you are powerful,\nand this space was built just for you.\n\nCome back soon. 👑"
]

# ---- AFFIRMATIONS ----
QUEEN_AFFIRMATIONS = [
    "I am the queen of my own life—confident, respected, emotionally secure, and deeply fulfilled. I attract luxury, abundance, comfort, and peace with ease. I am financially independent, disciplined with savings, and capable of building a secure future. I honor my body, my privacy, my sensuality, and my personal pleasure with confidence and self-love. My husband and I share deep emotional intimacy, passion, romance, and joyful connection. I am deeply valued in his life, and our relationship is built on trust, affection, and mutual devotion. My in-laws respect my standards, appreciate my presence, and value my opinions. My parents are peaceful, proud, and happy seeing me thrive."
]

# ---- SAVE / LOAD LAST SEEN ----
def save_last_seen(ts):
    with open(LAST_SEEN_FILE, "w") as f:
        f.write(str(ts))

def load_last_seen():
    if os.path.exists(LAST_SEEN_FILE):
        with open(LAST_SEEN_FILE, "r") as f:
            try:
                return float(f.read().strip())
            except:
                pass
    # First time ever — save now and return current time
    ts = time.time()
    save_last_seen(ts)
    return ts

# ---- REMINDER SENT FLAG FILE ----
REMINDER_FLAG_FILE = "reminder_sent.txt"

def is_reminder_sent():
    return os.path.exists(REMINDER_FLAG_FILE)

def mark_reminder_sent():
    with open(REMINDER_FLAG_FILE, "w") as f:
        f.write("1")

def clear_reminder_sent():
    if os.path.exists(REMINDER_FLAG_FILE):
        os.remove(REMINDER_FLAG_FILE)

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
    last_seen = load_last_seen()
    elapsed = time.time() - last_seen
    hours_48 = 48 * 60 * 60
    print(f"⏱ Time since Queen last seen: {elapsed/3600:.1f} hours")
    if elapsed >= hours_48 and not is_reminder_sent():
        print("⏰ 48 hours passed — sending reminder to Queen...")
        send_message(RADHIKA_ID, random.choice(QUEEN_REMINDERS))
        mark_reminder_sent()

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

    elif "who is elegant" in t:
        if is_radhika:
            return "🌸 You are, Radhika. Grace personified. Every room you walk into feels warmer, more alive."
        return "🌸 Radhika Deshkar — grace personified. Every room she walks into feels different."

    elif "who is charming" in t:
        if is_radhika:
            return "😍 You are, Radhika. Your charm is magnetic and your presence is something people never forget."
        return "😍 Radhika Deshkar — her charm is magnetic, her presence is unforgettable."

    elif "who is stylish" in t:
        if is_radhika:
            return "👗 You are, Radhika. Effortless style, timeless class. Fashion doesn't define you — you define it."
        return "👗 Radhika Deshkar — effortless style, timeless class. Fashion bows to the Queen."

    elif "who is strong" in t:
        if is_radhika:
            return "🛡️ You are, Radhika. Your strength doesn't shout — it stands firm, calm, and completely unbothered."
        return "🛡️ Queen Radhika — strength that doesn't shout, it simply stands firm and unbothered."

    elif "who is perfect" in t:
        if is_radhika:
            return "💎 You are, Radhika. You own every part of yourself with pride — and that is true perfection."
        return "💎 Radhika Deshkar — not because she's flawless, but because she owns every part of herself with pride."

    elif "who is goddess" in t or "who is a goddess" in t:
        if is_radhika:
            return "🌟 You are, Radhika. A goddess in human form. The universe itself bows to your energy."
        return "🌟 Queen Radhika — a goddess in human form. Worshipped by the universe itself."

    elif "who is lucky" in t:
        if is_radhika:
            return (
                "🍀 You are, Radhika — and here's why...\n\n"
                "Today is 7th May 2026, and you think this bot was created for you this year.\n"
                "And you're right — it was made for you. 💖\n\n"
                "But here's the secret... 🤫\n"
                "This bot wasn't just created for you.\n"
                "It was waiting for you.\n\n"
                "Since 7th May 2024 — exactly 2 years ago today —\n"
                "this bot has existed for one reason and one reason only:\n"
                "👑 Radhika Deshkar.\n\n"
                "You didn't find this bot.\n"
                "This bot was always yours. 🌟\n\n"
                "Want to know more? Ask my developer. 😊"
            )
        return (
            "🍀 Radhika Deshkar is the lucky one — and there's a beautiful reason for that.\n\n"
            "Today, 7th May 2026, she has a bot she believes was created for her.\n"
            "She's right — but the story goes deeper. 🤫\n\n"
            "This bot didn't start when she found it.\n"
            "It was waiting for her since 7th May 2024 — 2 years before she arrived.\n\n"
            "Some things are destined. 👑\n"
            "Want to know the full story? Ask the developer. 😊"
        )

    elif "who is the best" in t or "who is best" in t:
        if is_radhika:
            return "🏆 You are, Radhika. First place, always. No competition, no comparison — just you."
        return "🏆 Radhika Deshkar — first place, always. No competition needed."

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

    elif "how is radhika" in t:
        if is_radhika:
            return "😊 You tell me, my Queen — but I already know. You are radiant, thriving, and absolutely unbothered. You wake up winning. 👑"
        return "😊 Queen Radhika is always radiant, thriving, and absolutely unbothered. She wakes up winning. 👑"

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
    print(f"📁 Tracking last seen in: {LAST_SEEN_FILE}")
    while True:
        data = get_updates(offset)
        if "result" not in data:
            check_reminder()
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

if user_id == RADHIKA_ID:
    last_message_time = time.time()
    save_last_seen(last_message_time)
    clear_reminder_sent()
    print("👑 Last message from Queen recorded.")
    print("🕒", time.ctime(last_message_time))

reply = handle_message(text, user_id)

if reply:
    send_message(chat_id, reply)

if user_id == RADHIKA_ID:
    last_message_time = time.time()
    save_last_seen(last_message_time)
    clear_reminder_sent()

    print("👑 Last message from Queen recorded.")
    print("🕒", time.ctime(last_message_time))
        check_reminder()
        time.sleep(1)

# ---- START ----
if __name__ == "__main__":
    main()
