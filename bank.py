print("assalomu alaykum👋 ")


   
a=int(input("Tilni tanlang: 1,Uzb. 2,Ingiliz. 3,Rus: " ))
if a==1:
    print("Assalomu alaykum siz ozbek tilini tanladingiz.")
    parol=float(input("Iltimos parolingizni kiriting: "))
elif a==2:
    print("Hello! You have selected the English language.")
    parol=float(input("Please enter your password: "))
elif a==3:
    print("Здравствуйте! Вы выбрали русский язык.")
    parol=float(input("Пожалуйста, введите ваш пароль: "))
else:
    print("Kechirasiz bunday til royhatda  yoq❗\n" 
    "Sorry, this language is not available in the list❗\n"
    ".Извините, этого языка нет в списке❗\n")
    exit()
if parol==1234:
    if a==1 :
        print("Menyu:\n1. Balans\n2. Pul yechish.")
        tanlov=int(input("Menyudan birni tanlang: "))
        if tanlov == 1:
            print("Sizning balansingiz: 1 500 000 so'm")
        elif tanlov == 2:
            print("Pul yechish bo‘limi.")
            summa=int(input("Qancha pul yechmoqchi siz: "))
            balans=1500000
            if 0<summa<balans:
                balans-=summa
                print(f"iltimos pulni oling:{summa} som.\n qoldiq:{balans} som .")
            else:   print("Mablag' yetarli emas❗")
        
        else:
            print("Bunday bo‘lim yo‘q!")
        
    elif a==2 :
        print("Menu:\n1. Balance\n2. Withdraw.")
        tanlov=int(input("Select an option from the menu: "))
        if tanlov== 1:
            print("Your balance is: 1,500,000 UZS")
        elif tanlov == 2:
            print("Withdraw section.")
            summa = int(input("How much money would you like to withdraw? "))
            balance = 1500000

            if 0 < summa < balance:
                balance -= summa
                print(f"Please take your cash: {summa} UZS.\nRemaining balance: {balance} UZS.")
            else:   print("Insufficient funds❗")
        else:
            print("Invalid option!")
    elif a==3 :
        print("Меню:\n1. Баланс\n2. Снять деньги.")
        tanlov=int(input("Выберите пункт меню: "))
        if tanlov == 1:
            print("Ваш баланс: 1 500 000 сум")
        elif tanlov == 2:
            print("Раздел снятия денег.")
            summa = int(input("Сколько денег вы хотите снять? "))
            balance = 1500000

            if 0 < summa < balance:
                balance -= summa
                print(f"Пожалуйста, заберите ваши деньги: {summa} сум.\nОстаток на счёте: {balance} сум.")
            else:
                print("Недостаточно средств❗")

        else:
            print("Такого раздела нет!")
        
else:
    if a==1:    print("Parol noto'g'ri❌")
    elif a==2:  print("Incorrect password❌")
    elif a==3:  print('Неверный пароль❌')