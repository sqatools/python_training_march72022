temp=5
for i in range(1,6):
    for j in range(i):
        if (temp%5==0):
            print(temp,end=" ")
            temp = temp +5
    print("\n")
for i in range(4,0,-1):
    for j in range(i):
        if (temp%5==0):
            print(temp-10, end=" ")
            temp = temp - 5
    print("\n")



