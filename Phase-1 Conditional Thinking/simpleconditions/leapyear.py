num = int(input("Enter a number: "))
if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
    print("the year is a leap year")
else:
    print("the year is not a leap year")