contacts = []  

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    print(f"✅ Contact '{name}' added successfully!\n")
    print(contact)

def view_contacts():
    if not contacts:
        print("📭 No contacts found.\n")
        return
    print("\n📒 Contact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']}")
    print()

def search_contact():
    search_name = input("Enter name to search: ").lower()
    
    for contact in contacts:
        if contact["name"].lower() == search_name:
            print(f"✅ Found: {contact['name']} | {contact['phone']} | {contact['email']}\n")
            break
        else:
            print("❌ Contact not  found.\n")

def delete_contact():
    del_name = input("Enter name to delete: ").lower()
    for contact in contacts:
        if contact["name"].lower() == del_name:
            contacts.remove(contact)
            print(f"🗑 Contact '{contact['name']}' deleted successfully!\n")
            return
    print("❌ Contact not found.\n")

def main():
    while True:
        print("=== 📞 Contact Book ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("⚠ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
