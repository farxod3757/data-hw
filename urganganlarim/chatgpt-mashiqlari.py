# # Foydalanuvchi matn kiritadi.

# # Dastur quyidagilarni chiqaradi:

# # nechta harf

# # nechta unli harf

# # nechta bo‘sh joy

# # nechta so‘z
# unli="a,u,e,i,o,A,U,E,I,O"
# soz = input("sozni kiriting: ")
# bosh_joy=soz.count(" ")
# matn_uzunliki=len(soz)
# harflar_soni=matn_uzunliki-bosh_joy
# sozlar_soni=len(soz.split())
# unli_harflar=0
# for harf in soz:
#     if harf in "a,u,e,i,o,A,U,I,E,O":
#         unli_harflar=unli_harflar+1
# print(f"harflar soni: {harflar_soni}\nunli harflar soni: {unli_harflar}\nbosh joylar soni: {bosh_joy}\nsozlar soni: {sozlar_soni}")


# matin=input("matin kiriting: ")
# matin=matin.split()
# uzun_soz=""
# for soz in matin:
#     for sozlar in matin:
#         if len(soz)>len(uzun_soz):
#             uzun_soz=soz
# print(uzun_soz)
    
        
matn = "Men bugun Python dasturlashni o‘rganishga qaror qildim va har kuni yangi narsalarni amaliyotda sinab ko‘raman"
matn=matn.split()
uzun_soz=""
eng_uzun_soz=""
for soz in matn:
    for sozlar in matn:
        if len(soz)>len(uzun_soz):
            uzun_soz=soz
            eng_uzun_soz=uzun_soz
        elif len(soz)==len(eng_uzun_soz):
            eng_uzun_soz=eng_uzun_soz+"\n"+uzun_soz
print(eng_uzun_soz)
    

