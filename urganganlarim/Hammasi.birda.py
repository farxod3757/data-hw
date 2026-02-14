import os
import requests
from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path

# ========== ENV YUKLASH ==========
BASE_DIR = Path(__file__).resolve().parent
env_path = BASE_DIR / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("API_KEY")

if not api_key:
    print("❌ API key topilmadi! .env faylni tekshiring.")
    print("Current path:", os.getcwd())
    print("Env path:", env_path)
    exit()

client = OpenAI(api_key=api_key)

# ========== MENU ==========
print("Assalomu alaykum")
print("⟪Hammasi birda⟫ dasturiga xush kelibsiz")
print("1 - Kalkulator")
print("2 - Chat bot")
print("3 - Valyuta kursi")
print("0 - Chiqish")

try:
    tanlov = int(input("Qaysi xizmatni tanlaysiz: "))
except ValueError:
    print("❌ Faqat raqam kiriting")
    exit()

# ========== 1. KALKULATOR ==========
if tanlov == 1:
    print("⟪Kalkulator⟫")
    amal = input("Amalni tanlang (+, -, *, /, tub): ").lower()

    if amal == "tub":
        a = int(input("Son kiriting: "))
        if a <= 1:
            print("Tub son emas ❌")
        else:
            tub = True
            for i in range(2, int(a**0.5) + 1):
                if a % i == 0:
                    tub = False
                    break
            print("Tub son ✅" if tub else "Tub son emas ❌")

    elif amal in ["+", "-", "*", "/"]:
        a = float(input("1-sonni kiriting: "))
        b = float(input("2-sonni kiriting: "))

        if amal == "+":
            print("Natija:", a + b)
        elif amal == "-":
            print("Natija:", a - b)
        elif amal == "*":
            print("Natija:", a * b)
        elif amal == "/":
            if b == 0:
                print("0 ga bo‘lish mumkin emas ❌")
            else:
                print("Natija:", a / b)
    else:
        print("Bunday amal yo‘q ❌")

# ========== 2. CHAT BOT ==========
elif tanlov == 2:
    print("Chat botga xush kelibsiz (exit — chiqish)")
    messages = []

    while True:
        user_input = input("Siz: ")

        if user_input.lower() == "exit":
            print("Chat tugadi 👋")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages
            )

            bot_reply = response.choices[0].message.content
            print("Bot:", bot_reply)

            messages.append({"role": "assistant", "content": bot_reply})

        except Exception as e:
            print("❌ API xatolik:", e)

# ========== 3. VALYUTA ==========
elif tanlov == 3:
    from_currency = input("Qaysi valyutadan (masalan USD): ").upper()
    to_currency = input("Qaysi valyutaga (masalan UZS): ").upper()

    url = f"https://open.er-api.com/v6/latest/{from_currency}"

    try:
        data = requests.get(url).json()

        if data.get("result") == "success":
            rate = data["rates"].get(to_currency)

            if rate:
                print(f"1 {from_currency} = {rate} {to_currency}")
            else:
                print("Valyuta topilmadi ❌")
        else:
            print("API xato ❌")

    except Exception as e:
        print("❌ Internet yoki API xato:", e)

# ========== CHIQISH ==========
elif tanlov == 0:
    print("Dasturdan chiqildi 👋")

else:
    print("Noto‘g‘ri tanlov ❌")
