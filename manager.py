import utilities

class Manager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.balance = 0.0
        self.warehouse = {}
        self.history = []
        self.actions = {}
        self.load_data()

    def assign(self, name, func):
        self.actions[name] = func

    def execute(self, name):
        if name in self.actions:
            self.actions[name](self)
        else:
            print(f"Error: Command '{name}' not found.")

    def load_data(self):
        try:
            with open(self.file_path, "r") as file:
                for line in file:
                    line = line.strip()
                    if line.startswith("BAL:"):
                        self.balance = float(line.replace("BAL:", ""))
                    elif line.startswith("INV:"):
                        parts = line.replace("INV:", "").split(",")
                        # nome: [prezzo, quantità]
                        self.warehouse[parts[0]] = [float(parts[1]), int(parts[2])]
                    elif line.startswith("HIS:"):
                        self.history.append(line.replace("HIS:", ""))
        except FileNotFoundError:
            print("Database not found. Starting with empty records.")

    def save_data(self):
        with open(self.file_path, "w") as file:
            file.write(f"BAL:{self.balance}\n")
            for product, info in self.warehouse.items():
                file.write(f"INV:{product},{info[0]},{info[1]}\n")
            for event in self.history:
                file.write(f"HIS:{event}\n")
        print("Data saved successfully.")


manager = Manager("dbfile.txt")

manager.assign("balance", utilities.action_balance)
manager.assign("sale", utilities.action_sale)
manager.assign("purchase", utilities.action_purchase)
manager.assign("account", utilities.action_account)
manager.assign("list", utilities.action_list)
manager.assign("save", utilities.action_save)

while True:
    print(f"\nAvailable: {', '.join(manager.actions.keys())}, end")
    cmd = input("Insert Command: ").strip().lower()

    if cmd == "end":
        manager.save_data()
        print("Good bye!")
        break

    manager.execute(cmd)