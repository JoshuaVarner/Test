while True:
    try:    
        num = float(input("Enter a number: "))
    except ValueError:
        print("input is not a number")
        continue
    else:
        if (num % 2) == 0:
            print(str(num) + " is Even")
        else:
            print(str(num) + " is Odd")
