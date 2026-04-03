# print(23==23 and 32!=34 or 48<50 and 100<20 or not 48<11 or 1>5)
#       true and true  
#           ture or true
#                True and False
#                     False or True 
#                         True or False
 #                             ptint(  True  )
# print(23>22 or (200==211 and 18==21-3) or (33!=81 and 59<20) or 346-22>=324)
    #    True    or     False
                             # True or False
                                            #  True or True
                                                             #  True

# yosh = int (input("yoshingizni kiriting: "))
# if yosh < 18:
#     print("kirish taqiqlanadi!")
# elif yosh==18:
#     print("sizga 10 foiz sikitka bor🎉")
# else:
# #    print ("kirish mumkin !")
sorov=int(input("kilametrni tanlaysizmi 1 sonini kiriting\n metrni tanlasangiz 2 sonini kiriting: "))
if sorov==1:
    print(float(input("kilometrni kiriting: ")),sorov/1000,"metr")
else:
    print(float(input("metrni kititing: ")), sorov*1000/1,"km")