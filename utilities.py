def action_balance(manager):
    value = input("Insert amount to Add or subtract: ")
    try:
        amount = float(value)
        manager.balance += amount
        manager.history.append(f"Balance update: {amount}")
    except ValueError:
        print("Error: Insert a correct numeric value.")


def action_sale(manager):
    product = input("Product name: ")
    try:
        price = float(input("Selling Price: "))
        quantity = int(input("Quantity: "))

        if product in manager.warehouse and manager.warehouse[product][1] >= quantity:
            manager.warehouse[product][1] -= quantity
            manager.balance += (price * quantity)
            manager.history.append(f"Sold: {product} x{quantity}")
        else:
            print("Error: Product not in stock or insufficient quantity.")
    except ValueError:
        print("Error: Invalid price or quantity.")


def action_purchase(manager):
    product = input("Select Product: ")
    try:
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))
        total = price * quantity

        if manager.balance >= total:
            manager.balance -= total
            if product in manager.warehouse:
                manager.warehouse[product][1] += quantity
            else:
                manager.warehouse[product] = [price, quantity]
            manager.history.append(f"Purchase: {product} x{quantity}")
        else:
            print("Error: Insufficient balance.")
    except ValueError:
        print("Error: Invalid input.")


def action_account(manager):
    print(f"Current Balance: {manager.balance}")


def action_list(manager):
    print("Warehouse status:")
    for name, info in manager.warehouse.items():
        print(f"- {name}: {info[1]} units at {info[0]}€")


def action_save(manager):
    manager.save_data()
    print(">>> Backup completed: data saved on dbfile.txt")