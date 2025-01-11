

# add items to the list, remove items, and display the current list.

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        try:
            display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                # Prompt for and add an item
                new_item = input("Enter the item name: ")
                shopping_list.append(new_item)

            elif choice == '2':
                # Prompt for and remove an item
                item = input("Enter the item name: ")
                if item in shopping_list:
                    shopping_list.remove(item)
                else:
                    print("this item is not in shopping list")
                
            elif choice == '3':
                # Display the shopping list
                for item in shopping_list:
                    print(item)
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError as e:
            print(f'there is an error: {e}')


main()