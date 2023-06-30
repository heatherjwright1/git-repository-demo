## Task 3
## Create a dictionary with a minimum of 3 items and prices
## One of the items needs to cost more than £100
#Note for instructor: I completed this in a separate file called 'practice' which can also be seen via git repository demo

items = {
    'shoes': 149,
    'jacket': 160, 
    'hoodie': 36
}

available_money = 100
purchase_attempts = 0

print("Welcome to the store! Here are the items available: ")
for item, price in items.items():
    print(f"{item}: £{price}")

while True:
    user_input = input("Which item would you like to purchase? (Please ensure you input in lower case). If you would like to leave the store please input 'exit': ")
    
    if user_input == 'exit':
        print("Thank you for leaving the store. Goodbye!")
        break
        
    if user_input not in items: 
        raise ValueError("Sorry, this item is not available at our store.")
    
    price = items[user_input]
    
    if price <= available_money:
        print(f"You can purchase this item {user_input}. Thank you!")
        break
    
    ask_more_money = input("Sorry, you do not have enough money for this item. Would you like to add more to your balance? Answer either 'yes' or 'no' to continue:")
    
    if ask_more_money == 'yes': 
        try: 
            amount = int(input("Please enter an amount to add to your balance: £"))
            new_balance = available_money + amount
            
            if price <= new_balance:
                purchase_attempts += 1
                print(f"You can purchase this item {user_input}. Thank you!")
                break
            else:
                if purchase_attempts >= 3:
                    print("Sorry, you can only try 3 times to purchase this item, goodbye!")
                    raise ValueError("Please enter a valid amount (must be £1 minimum)")
        except ValueError:
            print("Please enter a valid amount (must be a number)")
            
    elif ask_more_money == 'no':
        print("Goodbye")
        break

print("Thank you for shopping at our store!")
