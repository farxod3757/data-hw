# students.json fayl yaratish uning ichida 20 
# ta o'quvchini ism familya yosh bn yaratish 

# kod orqali shu faylni oqib olish va 14 yoshdan katta 
# bo'lgan o'quvchilarni sorted_students.json faylga qoshish
import json
with open("students.json","r") as talabalar:
    tozalangan_t=[]
    oquvchilar=json.loads(talabalar.read())
    for oquvchi in oquvchilar:
        if oquvchi["yosh"]>14:
            tozalangan_t.append(oquvchi)
with open("sorted_students.json","w") as f:
    yangi_oquvchilar=json.dumps(tozalangan_t)
    f.write(yangi_oquvchilar)

