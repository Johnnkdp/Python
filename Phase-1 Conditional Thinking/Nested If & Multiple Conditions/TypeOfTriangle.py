a = int(input("enter the side a "))
b = int(input("enter the side b "))
c = int(input("enter the side c "))
if( a + b > c and b + c > a and c + a > b) :
    print("Valid Triangle")
    if( a==b==c):
        print("Equilateral Triangle")
    elif( a==b or b==c or c==a):
        print("Isoceles Triangle")
    else:
        print("Scalene Triangle")