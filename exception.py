try:
    n1=int(input())
    n2=int(input())
    result=n1*n2
    print(f"the result is {result}")
except ValueError:
    print("error is occured")
else:
    print("no error")
finally:
    print("end of the program")