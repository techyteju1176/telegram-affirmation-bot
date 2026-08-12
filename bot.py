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

# ---- QUEEN STORY ----
QUEEN_STORY = (
    "👑 The Story of Radhika — The Queen Within\n\n"
    "Radhika's story is not really about a crown placed upon her head by someone else. "
    "It is about a woman who gradually discovers that the crown was within her all along. "
    "What makes her special is not simply how she appears to the world, but the depth of "
    "what she carries inside—her ability to nurture, protect, love, endure, and continue "
    "moving forward even when life becomes demanding. She has the heart of someone who "
    "naturally wants the people she cares about to be safe, supported, and happy. Her "
    "presence can bring warmth and emotional richness into the lives around her.\n\n"
    "But being a Queen is not always easy. Behind every beautiful crown there can be "
    "responsibilities, expectations, and moments when the weight becomes difficult to "
    "carry. Radhika's strength comes from learning how to continue without allowing "
    "difficult experiences to take away her dignity. Her strength is not about "
    "overpowering others. It is the quieter kind—the strength to remain composed, to "
    "recover, to keep her heart alive, and to find herself again after difficult "
    "chapters.\n\n"
    "There is also a deeply emotional side to her. She can care intensely, remember "
    "meaningful moments, and become attached to the people and relationships that "
    "matter to her. Her heart can be generous, sometimes even to the point of giving "
    "more than she receives. But part of becoming the Queen of her own life is learning "
    "that love does not require self-abandonment. She can care for others while still "
    "caring for herself. She can give without emptying herself. She can love without "
    "losing her identity.\n\n"
    "As she grows, another quality becomes increasingly important: boundaries. A Queen "
    "learns that kindness does not mean saying yes to everything. She learns that "
    "forgiveness does not require tolerating everything. She learns that protecting her "
    "peace is not selfish. She learns to distinguish between responsibilities that "
    "genuinely belong to her and burdens that she has simply become accustomed to "
    "carrying.\n\n"
    "There may be moments when even a strong woman wonders whether she is truly "
    "understood or appreciated. Someone can look confident from the outside while "
    "quietly carrying questions within: Does anyone see how much I have done? Does "
    "anyone understand what I feel? Am I valued for who I am, or only for what I do for "
    "others? But her greatest transformation comes when she realizes that her worth "
    "cannot depend entirely upon other people's recognition.\n\n"
    "She begins to understand something profound: her value does not increase when "
    "people praise her, and it does not disappear when people fail to appreciate her. "
    "She does not need to constantly prove that she deserves respect, love, or "
    "happiness. The more peacefully she accepts her own worth, the less she needs the "
    "world to confirm it.\n\n"
    "That is when her crown becomes lighter.\n\n"
    "She becomes a woman who can be soft without being weak, strong without becoming "
    "harsh, loving without losing herself, and independent without closing her heart. "
    "She can forgive while maintaining boundaries. She can care for others while "
    "protecting her own peace. She can carry responsibility without believing that she "
    "must carry everything alone.\n\n"
    "And perhaps that is what truly makes Radhika a Queen.\n\n"
    "Not because she rules over others, but because she learns to rule her own inner "
    "kingdom.\n\n"
    "Her crown is made of resilience.\n"
    "Her strength is made of courage.\n"
    "Her heart is made of compassion.\n"
    "Her wisdom is made of experience.\n"
    "Her dignity is made of self-respect.\n"
    "And her greatest beauty is the moment she finally realizes that she never needed "
    "anyone else's permission to shine.\n\n"
    "A Queen is not the woman who makes everyone bow before her. A Queen is the woman "
    "who knows her worth, protects her peace, loves with a full heart, rises after "
    "difficult chapters, and walks through life with the quiet knowledge that her light "
    "belongs to her. 👑✨"
)

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

    # ---- WHY / WHAT MAKES RADHIKA A QUEEN ----
    elif "why is radhika queen" in t or "why radhika is queen" in t or "what makes radhika" in t or "why is radhika a queen" in t:
        return QUEEN_STORY

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

