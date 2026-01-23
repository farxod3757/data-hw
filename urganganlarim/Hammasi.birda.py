import requests
import openai

print("Assalomu alaykum\n⟪Hammasi birda⟫ dasturiga xush kelibsiz")
print("1-Kalkulator\n2-Chat bot\n3-Valyuta kursi\n0-Chiqish")

tanlov = int(input("Qaysi xizmatni tanlaysiz: "))
if tanlov == 1:
    print("⟪Kalkulator⟫")
    amal = input("Amalni tanlang (+, -, *, /, tub): ").lower()

    if amal == "tub":
        a = int(input("Son kiriting: "))
        if a <= 1:
            print("Tub son emas")
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

elif tanlov == 2:
    print("Chat botga xush kelibsiz (exit — chiqish)")
    client = openai.OpenAI(api_key="API_KEYINGNI_BU_YERGA_QOY")

    while True:
        user_input = input("Siz: ")
        if user_input.lower() == "exit":
            break

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": user_input}]
        )
        print("Bot:", response.choices[0].message.content)


elif tanlov == 3:
    from_currency = input("Qaysi valyutadan masalan (USD): ").upper()
    to_currency = input("Qaysi valyutaga masalan (UZS): ").upper()

    url = f"https://open.er-api.com/v6/latest/{from_currency}"
    data = requests.get(url).json()

    if data["result"] == "success":
        rate = data["rates"].get(to_currency)
        if rate:
            print(f"1 {from_currency} = {rate} {to_currency}")
        else:
            print("Valyuta topilmadi ❌")
    else:
        print("API xato ❌")

elif tanlov == 0:
    print("Dasturdan chiqildi 👋")

else:
    print("Noto‘g‘ri tanlov ❌")
