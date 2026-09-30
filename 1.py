school_bag = ["Math Book", "English Notebook", "Pencil Box", "Water Bottle"]

while True:
    print("\n ===== SCHOOL BAG CHECKLIST =====")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Bag")
    print("4. Count Items")
    print("5. Search Item")
    print("6. Sort Bag Alphabetically")
    print("7. Clear Entire Bag")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item name: ")
        if item in school_bag:
            print(f"'{item}' is already in your bag!")
        else:
            school_bag.append(item)
            print(f"'{item}' added successfully.")
            
    elif choice == "2":
        item = input("Enter item to remove: ")
        if item in school_bag:
            school_bag.remove(item)
            print(f"'{item}' removed successfully.")
        else:
            print("Item not found.")
            
    elif choice == "3":
        print("\n Items in School Bag:")
        if len(school_bag) == 0:
            print("Bag is empty.")
        else:
            for index, item in enumerate(school_bag, 1):
                print(f"{index}. {item}")
                
    elif choice == "4":
        print("Total Items:", len(school_bag))
        
    elif choice == "5":
        item = input("Enter item to search for: ")
        if item in school_bag:
            print(f"Yes, '{item}' is in your bag.")
        else:
            print(f"No, '{item}' was not found in your bag.")
            
    elif choice == "6":
        if len(school_bag) == 0:
            print("Bag is empty. Nothing to sort.")
        else:
            school_bag.sort()
            print("Bag items sorted alphabetically.")
            
    elif choice == "7":
        confirm = input("Are you sure you want to clear the entire bag? (yes/no): ")
        if confirm.lower() == "yes":
            school_bag.clear()
            print("Bag cleared successfully.")
        else:
            print("Action cancelled.")
            
    elif choice == "8":
        print("Thank you! Have a great day at school!")
        break
        
    else:
        print("Invalid Choice. Please try again.")
