try:
    n1 = int(input("Enter number1: "))
    n2 = int(input("Enter number2: "))
    result = n1 % n2
    print(f"{result}")
except Exception as error:
    print(f" Error occurred", error)
finally:
    print("End of program")