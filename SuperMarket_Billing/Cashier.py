def billing(prod):
    Temp = 0.0
    purchase = {}
    print("\n\nEnter the Purchases of customer...\n")
    while True:
        print("")
        product = input("Enter Purchased item(Enter Q to Quit): ").capitalize()
        if product == "Q":
            break
        if product not in prod:
            print("Sorry, the item is currently unavailable!!\n")
            continue
        try:
            quantity = int(input("Quantity: "))
            if quantity <= 0:
                print("Quantity must be a positive integer.\n")
                continue
        except ValueError:
            print("Invalid input! Please enter a valid integer for quantity.\n")
            continue
        Temp += quantity * prod[product]
        purchase[product] = purchase.get(product, 0) + quantity
    if not purchase:
        print("\nNo items purchased.\n\nThank You!!\nPlease visit again!!\n\n")
        return
    while True:
        member = input("\nMembership Card (Gold, Silver, Bronze, or None): ").capitalize().strip()
        if member in {"Gold", "Silver", "Bronze", "None"}:
            break
        else:
            print("Invalid membership type! Please enter Gold, Silver, Bronze, or None.\n")
    Total = Temp
    membership = {"Gold": 0.80, "Silver": 0.90, "Bronze": 0.95, "None": 1.0}

    print("\n\nTotal Bill:\n")
    print("Item\tQuantity\tUnit Price\tSubtotal\n------------------------------------------------\n")
    for key, value in purchase.items():
        print(f"{key}\t{value}\t\t₹{prod[key]}\t\t₹{value * prod[key]}\n")
    if Total >= 500 and not(member == "None"):
        discount = membership.get(member, 1.0)
        Total = Temp * discount
        print(f"\nYour discount of {100-((membership.get(member))*100)}% is applied successfully!!")
    else:
         print("\nMinimum purchase of ₹500 is required to apply discount...")
    print(f"\nTotal Amount before Discount: ₹{Temp}\n")
    print(f"Total payable amount after Membership card: ₹{Total}\n\n\nThank You!!\nPlease visit again!!\n\n")


def manager():
    avail = {}
    print("\nEnter available product and their cost one by one..")
    while True:
        print("")
        product = input("Enter available product(Enter Q to quit): ").capitalize()
        if product == "Q":
            break
        try:
            amount = int(input("Enter the cost of product in Rupees: "))
            if amount <= 0:
                print("Price must be a positive integer.\n")
                continue
        except ValueError:
            print("Invalid input! Please enter a valid integer for price.\n")
            continue
        if product in avail:
            print("Item already registered!\n")
        else:
                avail[product] = amount
    print("\nAvailable Stock\n\nItem\tMRP\n------------\n")
    for key, value in avail.items():
        print(f"{key}\t{value}\n")
    billing(avail)


def default():
    print("Available Stock\n\nItem\tMRP\n------------\n")
    avail = {"Milk": 30, "Bread": 40, "Egg": 10, "Rice": 80, "Sugar": 45, "Oil": 120}
    for key, value in avail.items():
        print(f"{key}\t₹{value}\n")
    print("\n")
    billing(avail)


print("\n\nWelcome to Kirthan's Super-Market Cashier Project!!!\n")
while True:
    a = input("\nUse Default available stock: Enter(A)\nCreate new stock list: Enter(B)\nEnter: ").capitalize().strip()
    if a == "B":
        manager()
        break
    elif a == "A":
        default()
        break
    else:
        print("Invalid Input! Please enter A or B.\n")
