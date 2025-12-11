print("enter three numbers")
a = int(input())
b = int(input())
c = int(input())
if a > b:
    if a > c:
        print("largest number" + str(a))
    else:
        print("the largest number" + str(a))
else:
    if c > b:
        print("the largest number" + str(c))
    else:
        print("the largestnumber" + str(b))
