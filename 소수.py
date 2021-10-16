num = int(input("enter num:"))
for i in range(2, num):
    temp = True
    for j in range(2, i):
        if i % j == 0:
            temp = False
            break
    if temp == True:
        print(i, "소수")
