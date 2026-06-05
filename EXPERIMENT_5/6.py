# 6- contact book
contacts = {}

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    contacts[name] = {"phone": phone, "email": email}
    print("Contact added.")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(name, ":", contacts[name])
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        phone = input("New phone (leave blank to keep same): ")
        email = input("New email (leave blank to keep same): ")
        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email
        print("Contact updated.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

while True:
    print("\n1.Add  2.Search  3.Update  4.Delete  5.Show all  6.Exit")
    ch = input("Choice: ")

    if ch == "1":
        add_contact()
    elif ch == "2":
        search_contact()
    elif ch == "3":
        update_contact()
    elif ch == "4":
        delete_contact()
    elif ch == "5":
        for name, info in contacts.items():
            print(name, ":", info)
    elif ch == "6":
        break
    else:
        print("Invalid choice")
