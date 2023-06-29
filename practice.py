items = {
    'shoes': 149,
    'jacket': 160,
    'hoodie': 36
}

available_money = 100
balance = 0
purchase_attempts = 0

print("Welcome to the store! Here are the items available:")
for item, price in items.items():
    print(f"{item}: £{price}")

while True:
    option = input("Which item would you like to purchase? (Please ensure you input in lower case), or type 'exit' to leave the store: ")

   

                purchase_attempts += 1
            except ValueError:
                raise ValueError("Invalid input. Please enter a valid amount.")
        elif additional_money == 'no':
            print("Thank you for visiting the store. Goodbye!")
            break
        else:
            raise ValueError("Invalid input. Please answer 'yes' or 'no'.")
