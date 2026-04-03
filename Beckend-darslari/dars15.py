#1=manfiy musbat❗
#  son=float(input(" sonni kiriting: "))
# if son>0:
#     print(" musbat son")
# elif son<0:
#     print(" manfiy son")
# else:   print("son 0")

# 2=18 yoshga kirishga mumkin❗
# yosh=int(input("yoshingizni kiriting: "))
# if yosh>=18:
#     print(" mumkin")
# else:   print("mumkin emas")

# 3=sonni kattasi❗
# son1=float(input("1 chi soni kiriting: "))
# son2=float(input("2 chi sonni kiriting: "))
# if son1>son2:
#     print("1 chi son katta ")
# elif son1<son2:
#     print("2 chi son katta")
# else:   print("2 son ham teng")


# 4=imtihon natijasi❗
# ball=int(input("balingizni kiriting: "))
# if ball>=50:
#     print("siz ottingiz🥳")
# else:   print("o'ta olmadingiz: ")


#o'rtachaaaa

# 1=3 ga va 5 ga bolinishi❗
# son=float(input(" son kiriting: "))
# if son%3==0:
#     print("bu son 3ga bolinadi:")
# elif son%5==0:
#     print("bu son 5 ga bolinadi: ")
# elif son%3==0 and son%5==0:
#     print("bu son 3 ga ham 5 ga ham bolinadi")
# else:   print("bu son 5 ga ham 3 ga ham bolinmaydi")

# 2=haroratni tekshirish❗
# temp=float(input("haroratni kiriting: "))
# if temp>=30:
#     print("harorat issiq")
# elif temp<15:
#     print("harorat souq")
# else:   print("harorat iliq")

# 3=kasiba yil❗
# yil=int(input("yilni kiriting: "))
# if yil%400==0 and yil%100==0 or yil%4==0:
#     print("kabisa yil")
# else:    print("kabisa yil emas")

# 4=1 va 100 orasidagi son❗
# son=float(input("sonni kiriting: "))
# if son>=1 and son<=100:
#     print("bu son 1 va 100 orasidagi son")
# else:   print("bu son 1 va yuz oraliqida emas")

# 5=kalkulyator❗
# a = float(input("1-sonni kiriting: "))
# amal=input("amalni tanlang!\n+\n-\n*\n/  siz:")
# b = float(input("2-sonni kiriting: "))

# if b == 0:
#     x=float(input("0 dan katta son kiriting: "))
#     if amal == "+":
#             print("Natija:", a + x)
#     elif amal == "-":
#             print("Natija:", a - x)
#     elif amal == "*":
#             print("Natija:", a * x)
#     elif amal == "/":
#         print("Natija:", a / x)
# elif amal == "+":
#             print("Natija:", a + b)
# elif amal == "-":
#             print("Natija:", a - b)
# elif amal == "*":
#             print("Natija:", a * b)
# elif amal == "/":
    
#      print("Natija:", a / b)
# else:
#      print("Bunday amal yo‘q ❌")

# 6=BMI❗
# try:
#     boy=float(input("Boyingiz nechi sm: "))

#     kilo=float(input("Vazningizni kiriting: "))
#     if kilo/(boy*boy)<18.5:
#          print("siz qoni kam siz😂")
#     elif kilo/(boy*boy)>=18.5 and kilo/(boy*boy)<=24.9:
#         print("normal vazin")
#     elif kilo/(boy*boy)>=25 and kilo/(boy*boy)<=29.9:
#         print("semizroq siz")
#     else:   print("yuqori semizlik")
# except ValueError:
#     print("Xatolik! Faqat son kiriting.")

# except ZeroDivisionError:
#     print("Xatolik! Bo'y 0 bo'lishi mumkin emas.")

# except Exception:
#     print("Noma'lum xatolik yuz berdi.")