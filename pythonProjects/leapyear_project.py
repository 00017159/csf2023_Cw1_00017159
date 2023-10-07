a = int(input("Number: "))
if a > 1582:
    if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0 or a % 1000 == 0:
        print("It is a leap year!")
    else:
        print("it is not a leap year")