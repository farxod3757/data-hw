a = int(input("sonni kiriting: "))

if a <= 1:
    print("tub son emas")
else:
    tub = True
    for i in range(2, a):
        if a % i == 0:
            tub = False
            break

    if tub:
        print("tub son")
    else:
        print("tub son emas")
