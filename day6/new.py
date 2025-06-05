import contacts as nw
contacts = {}
print("\tContacts App")

while True:
    try:
        print("\n\nChoices :")
        print("1. Add contact")
        print("2. View all contacts")
        print("3. Delete contact")
        print("4. Find contact")
        print("5. Edit contact")
        print("6. Exit")
        choice = int(input("Enter choice : "))

        if choice == 1:
            nw.add_contact(contacts)
        elif choice == 2:
            nw.view_contacts(contacts)
        elif choice == 3:
            nw.delete_contact(contacts)
        elif choice == 4:
            nw.find_contact(contacts)
        elif choice == 5:
            nw.edit_contact(contacts)
        else:
            print("End")
            break
    except Exception as error:
        print("Error found",error)
    finally:
        print("End of the program")