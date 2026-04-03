# try:
#     raqam=int(input("son kiriting: "))
#     if int(raqam):
#         raise Exception("intejer ms bu")

# except ValueError:
#     print("butun son kerak")

# else:
#     print("hatolik yoq")
# finally:
#     print("an")
# try:

#     son1=int(input("son kiriting: "))
#     son2=int(input("2chi son: "))
#     x=son1/son2
#     print(x)
# except ZeroDivisionError:
#     print("nolga bolish mumkin emas")
# except ValueError:
#     print("butun son bolishi kerak")

import requests
import json
try:
    response=requests.get("https://jsonplaceholder.typicode.com/posts/1")
    data=response.json()
    with open("qod.json","w") as f:
        f.write(json.dumps(data))
except:
    print("hato boldi")