contacts={}
while True:
    print( "=" * 40)
    print("        CONTACT BOOK")
    print("=" * 40)
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
    choice=input("Enter the your choice(1-6):")
    if choice=="1":
        name=input("Enter the name:")
        if name in contacts:
            print("Contact already exists!")
        else:
            phone = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            contacts[name] = {
                "Phone": phone,
                "Email": email,
                "Address": address
            }
            print("Contact added successfully!")
    
    elif choice=="2":
          if not contacts:
            print("No contacts found.")
          else:
            print("\nContact List")
            print("-" * 40)
            for name, details in contacts.items():
                print(f"Name : {name}")
                print(f"Phone: {details['Phone']}")
                print("="* 40)
    elif choice == "3":
        search = input("Enter Name or Phone Number: ")

        found = False

        for name, details in contacts.items():
            if search.lower() == name.lower() or search == details["Phone"]:
                print("\nContact Found")
                print("-" * 30)
                print("Name   :", name)
                print("Phone  :", details["Phone"])
                print("Email  :", details["Email"])
                print("Address:", details["Address"])
                found = True
                break

        if not found:
            print("Contact not found.")
    elif choice == "4":
        name = input("Enter Contact Name to Update: ")

        if name in contacts:
            phone = input("Enter New Phone Number: ")
            email = input("Enter New Email: ")
            address = input("Enter New Address: ")

            contacts[name]["Phone"] = phone
            contacts[name]["Email"] = email
            contacts[name]["Address"] = address

            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    elif choice == "5":
        name = input("Enter Contact Name to Delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    elif choice == "6":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")