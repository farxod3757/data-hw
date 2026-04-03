# 1."kitoblar.txt" fayliga 5 ta sevimli kitob 
# nomini yozing va keyin ularni o‘qib ekranga chiqaring

# with open("kitoblar.txt","a") as f:
#     f.write("Shum bola\nHarry Potter\nMuqaddima\nGeografiya mahkumlari\nSharq")
# with open("kitoblar.txt",) as f:
#     print(f.read())



# 2."baholar.txt" fayliga 5 ta
# baho yozing (masalan: 85, 90, 78, 100, 67) va keyin o‘qib o‘rtacha bahoni hisoblang.

# with open("baholar.txt","a") as baxolar:
#     baxolar.write("85\n78\n100\n90\n67")
# with open("baholar.txt") as baxolar:
#     sonlar=[]
    
#     for baxo in baxolar:
#         sonlar.append(int(baxo.strip))
#         sonlar.sort()
#     sonlar=(sonlar[len(sonlar)//2])
#     print(sonlar)



# 3."matn.txt" fayliga bir necha jumla 
# yozing va keyin o‘qib eng uzun so‘zni toping.

# with open("matn.txt","a") as matn:
    # matn.write("ser quyosh hur olkam elga baxtnajo")
# with open("matn.txt") as matn:
#     for soz in matn:
#         katta=[]
#         katta.append(soz)
#         katta=[(max(katta.split))]
# print(max(katta))

print(10/0)


    