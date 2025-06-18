def mail(name : str):
    if '@' in name and '.' in name:
        return True
    else:
        return False


email = input()
name = email[1:len(email)-1]
print(name,end = " ")

