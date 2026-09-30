menu={
    "apple":200.00,
    "banana":30.00,
    "milk":50.00,
    "bread":30.00,
    "chips":300.00
}

cart={}

def show_commands():
    """Displays user command option."""
    print("\n ---------- Chatbot Command ----------")
    print("1. 'menu'      -See available items & prices")
    print("2. 'add'       -Add an item to your cart")
    print("3. 'remove'    -Remove an item from your cart")
    print("4. 'view'      -Check your current cart contents")
    print("5. 'checkout'  -Print final receipt and exit")
    print("6. 'exit'      -Cancel and close chatbot")
    print("\n--------------------------------------")

print("Chatbot: Hello! Welcome to the PAA Classes Mart.")
print("Chatbot: I am your virtual shopping assistant.")
show_commands()

while True:
    user_action=input("\n You:").strip().lower()

    if user_action=="menu":
        print("\n --- Available Item Menu ---")
        for item,price in menu.items():
            print(f"-{item.capitalize()}: RS.{price:.2f}")

    elif user_action=="add":
        item_to_add=input("Chatbot: Which item do you want add?").strip().lower()
        if item_to_add in menu:
            try:
                qty=int(input(f"Chatbot: How many{item_to_add}s?"))
                if qty>0:
                    cart[item_to_add]=cart.get(item_to_add,0) + qty
                    print(f"Chatbot: Successfully addes {qty} {item_to_add}(s)!")
                else:
                    print("Chatbot: Please enter a quantity greater than zero.")
            except ValueError:
                print("Chatbot: Invalid count. Please enter a valid number.")
        else:
            print("Chatbot: Sorry,that item is not in our store catalog.")
    elif user_action=="remove":
        item_to_remove=input("Chatbot: Which item do you want remove?").strip().lower()
        if item_to_remove in cart:
            try:
                qty=int(input(f"Chatbot: How many {item_to_remove}s should I remove?"))
                if qty > 0:
                    if qty >= cart[item_to_remove]:
                        del cart[item_to_remove]
                        print(f"Chatbot: Removed all {item_to_remove}s from your cart.")
                    else:
                        cart[item_to_remove] -= qty
                        print(f"Chatbot: Removed {qty} {item_to_remove}(s) Remaining: {cart[item_to_remove]}")
                else:
                    print("Chatbot: Please specify a positive quantity.")
            except ValueError:
                print("Chatbot: Invalid number format.")
        else:
            print("Chatbot: That item is not present in your cart.")

    elif user_action=="view":
        if not cart:
            print("Chatbot: Your cart is currently empty.")
        else:
            print("\n --- Your Current Cart Items ---")
            subtotal = 0.0
            for item, quantity in cart.items():
                cost=menu[item] * quantity
                subtotal += cost
                print(f".{item.capitalize()} (x{quantity}): Rs. {cost:.2f}")
            print(f"Current Total: Rs. {subtotal:.2f}")
    elif user_action=="checkout":
        if not cart:
            print("Chatbot: Your cart is empty.Cannot checkout!")
        else:
            print("\n ============ FINAL RECIEPT ============")
            grand_total = 0.0
            for item, quantity in cart.items():
                cost=menu[item]*quantity
                grand_total += cost
                print(f" - {item.capitalize()} (x{quantity}): Rs.{cost:.2f}")
            print("=========================================")
            print(f"GRAND TOTAL BILL: Rs. {grand_total:.2f}")
            print("Chatbot: Thank you for shopping with PAA Classes Mart! Good Byee!")
            break
    elif user_action=="exit":
        print("Chatbot: Program closed. Thank You!")
        break
    else:
        print("Chatbot: Invalid command! Type 'menu','add','remove','view','checkout' or 'exit'.")
                    
