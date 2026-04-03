
# uy ishi
# 1= Karra jadvali: Faqat 10 soni uchun karra jadvalini (7x1 dan 7x10 gacha) to'liq chiqaring.
# for i in range(1,10):
#     for x in range(1,11):
#         if x==1:
#             print("____________\n",i,"lar\n____________")
#         print(i,"*",x,"=",i*x,)

# 2= Salom, Dunyo!: Ekranga "Men Pythonni o'rganyapman" 
# jumlasini tsikl orqali 20 marta chiqaring. (13 siklda chiqarmasn va 19 siklda toxtatsin)

# x="Salom, Dunyo!: Men Pythonni o'rganyapman"
# for i in range(1,21):
#     if i== 13:
#             continue
#     if i==20:
#         break
#     print(i,x)

# 3= Sonlarni o'tkazib yuborish: 1 dan 100 gacha bo'lgan sonlarni chiqaring, lekin 5 ga 
# bo'linadigan sonlar kelganda ularni tashlab o'tib keting (continue ishlating)

# for i in range(1,101):
#     if i%5==0:
#         continue
#     print(i)

# 3.  Koordinatalar: 2 ta son so’rimiz va shu sonlar gacha bo'lgan x va y o'qlari uchun barcha 
# nuqtalarni chiqaring (masalan: (0,0), (0,1), (0,2)...).(nested loop) (2 forni bir birini ichida ishlatish)
# son=int(input("1-son: "))
# son2=int(input("2-son: "))
# for i in range(son+1):
#     for x in range(son2+1):
#         print(i,x)




# 1.    Hard:
# Matritsa: 3x3 o'lchamdagi matritsani (ro'yxat ichidagi ro'yxat) ekranga chiroyli shaklda chiqaring.
# 1- uaul
#  print("1 2 3\n4 5 6\n7 8 9")
# 2-chi usul
# a="1 1 1"
# for i in range(3):
#     i=a
#     print(i)