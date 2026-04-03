# x="text.txt"
# import os 
# if os.path.exists(x):
#     os.remove(x)
# else:
#     print("bunday fayl mavjud emas")
# with open("test.txt","w") as f:
#     f.write("Mening ismim Farxod..")
import os
x="test.folder"
if os.path.exists(x):
    os.rmdir(x)
else:
    print("bunday papka yoq")
x="salom.txt"
with open(x,"a") as f:
    f.write("yangiboyev fa")


