import tkinter as tk

class WalletApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Wallet App")

        self.balance_label = tk.Label(master, text="Balance: $0.00")
        self.balance_label.pack()

        self.add_button = tk.Button(master, text="Add Money", command=self.add_money)
        self.add_button.pack()

        self.subtract_button = tk.Button(master, text="Subtract Money", command=self.subtract_money)
        self.subtract_button.pack()

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()

    def update_balance_label(self):
        self.balance_label.config(text="Balance: ${:.2f}".format(self.balance))

    def add_money(self):
        amount = float(input("Enter amount to add: "))
        self.balance += amount
        self.update_balance_label()
        print(add_money)

    def subtract_money(self):
        amount = float(input("Enter amount to subtract: "))
        if amount <= self.balance:
            self.balance -= amount
            self.update_balance_label()
        else:
            print("fuck you!")

def main():
    root = tk.Tk()
    app = WalletApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
