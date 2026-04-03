# def habar_ism(ism,xabar = "xayirli kun"):
#     return ism + " "+xabar
# ism=input("ism kiriting: " )
# xabar=input("habar kiriting:")
# print(habar_ism(ism,xabar)
def sonlar_orasi(min,max=100) : 
    l=0
    m=1
    for x in range(min,max+1):
        l=l+x
        l=l*2
    return l
min=int(input("son1: "))
max=int(input("saon2:"))
print(sonlar_orasi(min,max))