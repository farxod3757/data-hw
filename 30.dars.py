import json
# with open("settings.json","r") as f:
#     settings=json.loads(f.read())
#     print(settings["teme"])
# import json
with open("users.json") as f:
    users=json.loads(f.read())
    print(users[0]["ism"])
# user2={
#     "ism":"farxod",
#     "yosh":18
# }
# with open("yozsh.json","a") as f:
#     json_natija=json.dumps(user2)
#     f.write(json_natija)
# print(json.dumps(user2))
# mevalar=["anor","olma","nok","shaftoli"]
# with open("mevalar.json","a") as f:
#     mevalar2=json.dumps(mevalar)
#     f.write(mevalar2)
# print(json.dumps(mevalar))
with open("ismlar.json","r") as f:
    # yangi_ism=[]
    # while True:
    #  ismlar1=input("ism kiriting: ")
    #  if ismlar1=="q":
    #     break
    #  else:
    #     yangi_ism.append(ismlar1)
    # eng_yangiism=json.dumps(yangi_ism)
    # f.write(eng_yangiism)
    ismlar1=json.loads(f.read())
    print(ismlar1)