def add_contact(contacts):
        file = open("./new.txt","a")
        name = input("Enter Contact Name :")
        mobile = int(input("Enter mobile number :"))
        contacts[name] = mobile
        file.write(f"{name} : {mobile}\n")
        file.close()
def view_contacts(contacts):
    file = open("./new.txt","r")
    for i in contacts:
        print(f"{i} : {contacts[i]}")
        file.close()

def delete_contact(contacts):
    name = input("Enter contact name :")
    with open("./new.txt","a") as file:
        if name in contacts:
            del contacts[name]
            msg = f"Deleted contact:  {name}"
            print(msg)
            file.write(msg + "\n")
        else:
            msg = "No contact found"
            print(msg)
            file.write(msg + "\n")
def find_contact(contacts):
    name = input("Enter name to search : ")
    found = False
    with open("./new.txt","a") as file:
        for key in contacts:
            if name in key:
                msg = f"{key} : {contacts[key]}"
                print(msg)
                file.write(msg + "\n")
                found = True
        if not found:
            msg = "Not found"
            print(msg)
            file.write(msg + "\n")

def edit_contact(contacts):
    name = input("Enter contact name to edit :")
    with open("./new.txt","a") as file:
        if name in contacts:
            number = int(input("Enter new number: "))
            contacts[name] = number
            msg = f"edited contact:  {name}"
            print(msg)
            file.write(msg)
        else:
            msg = f"Not found"
            print(msg)
            file.write("./new.txt","a")
        