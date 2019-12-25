import random
x = random.randint(1, 100)
ans = 0
while ans == 0:
    n = int(input("請輸入猜測的值?"))
    if 0 < n < 101:
        if n < x:
            print("too small")
        elif n > x:
            print("too high")
        else:
            ans = 1
    else:
        print("wrong")
