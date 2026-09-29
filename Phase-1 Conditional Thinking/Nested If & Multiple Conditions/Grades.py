a = int(input("enter the marks"))
if a <0 or a >100:
    print("wrong")
else:
    if a >= 90:
        print("O")
    elif a >= 80:
        print("A+")
    else:
        print("F")