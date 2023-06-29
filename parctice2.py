## corect version!

items = {
    'shoes': 149,
    'jacket': 60,
    'hoodie': 36
}

available_money = 100
purchase_attempt = 0

print("Welcome to the store! Here are the items available:")
for item, price in items.items():
    print(f"{item}: £{price}")

while True:
  user_input = input("Which item would you like to purchase? (Please ensure you input in lower case). If you would like to leave the store please input 'exit': ")

if user_input in items:
    item = items[user_input]
    print(f"Great! The price of {user_input} is £{items[user_input]}.")

    if user_input == 'exit':
       print("Goodbye!")
       break

    if user_input not in items: 
       raise ValueError("Sorry, this item is not available at our store")
    
    price = items[user_input]
    if price <= available_money: 
     print(f"You can purchase this item {user_input}. Thank you!")  
    break


ask_more_money = input("Sorry, you do not have enough money for this item, would you like to add more to your balance? Answer either 'yes' or 'no' to continue:")

if ask_more_money == 'yes':
   try: 
      amount = (input("Please enter an amount to add to your balance: £"))
      new_balance = available_money + amount
    if price <= new_balance: 
       purchase_attempt += 1
     print(f"You can purchase this item {user_input}. Thank you!")  
    break


else: 
   if purchase_attempts >= 3:
      raise ValueError("Sorry, you can only try 3 times to purchase this item, goodbye!")

except ValueError:
raise ValueError("Please enter a valid amount (must be £1 minimum)")

   elif ask_more_money == "no":
print("Goodbye!")
break

