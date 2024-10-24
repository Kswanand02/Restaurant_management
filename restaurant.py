import tkinter as tk
from tkinter import messagebox


class RestaurantManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management System")
        self.root.geometry("600x600")

        # Menu items (separate for veg and non-veg)
        self.veg_menu = {
            'Paneer Tikka': {'price': 12, 'quantity': 0},
            'Veg Biryani': {'price': 10, 'quantity': 0},
            'Dal Tadka': {'price': 8, 'quantity': 0},
            'Aloo Gobi': {'price': 7, 'quantity': 0}
        }

        self.non_veg_menu = {
            'Chicken Biryani': {'price': 15, 'quantity': 0},
            'Butter Chicken': {'price': 18, 'quantity': 0},
            'Fish Curry': {'price': 14, 'quantity': 0},
            'Mutton Rogan Josh': {'price': 20, 'quantity': 0}
        }

        # Label for Veg Menu
        tk.Label(root, text="Veg Menu", font=('Arial', 14, 'bold')).grid(row=0, column=0, padx=10, pady=10)

        # Creating labels and entries for veg menu items
        self.veg_menu_entries = {}
        row = 1
        for item, details in self.veg_menu.items():
            tk.Label(root, text=f"{item} (₹{details['price']})").grid(row=row, column=0, padx=10, pady=5)
            self.veg_menu_entries[item] = tk.Entry(root, width=5)
            self.veg_menu_entries[item].grid(row=row, column=1, padx=10, pady=5)
            row += 1

        # Label for Non-Veg Menu
        tk.Label(root, text="Non-Veg Menu", font=('Arial', 14, 'bold')).grid(row=row, column=0, padx=10, pady=10)

        # Creating labels and entries for non-veg menu items
        self.non_veg_menu_entries = {}
        row += 1
        for item, details in self.non_veg_menu.items():
            tk.Label(root, text=f"{item} (₹{details['price']})").grid(row=row, column=0, padx=10, pady=5)
            self.non_veg_menu_entries[item] = tk.Entry(root, width=5)
            self.non_veg_menu_entries[item].grid(row=row, column=1, padx=10, pady=5)
            row += 1

        # Extras
        self.extra_var = tk.IntVar()
        tk.Label(root, text="Extra Cheese (+₹20)").grid(row=row, column=0, padx=10, pady=10)
        tk.Checkbutton(root, variable=self.extra_var).grid(row=row, column=1, padx=10, pady=10)
        row += 1

        # Buttons for generating and printing bill
        tk.Button(root, text="Generate Bill", command=self.generate_bill).grid(row=row, column=0, padx=10, pady=10)
        tk.Button(root, text="Print Bill", command=self.print_bill).grid(row=row, column=1, padx=10, pady=10)

        self.bill_text = tk.Text(root, height=10, width=40)
        self.bill_text.grid(row=row + 1, column=0, columnspan=2)

    def generate_bill(self):
        total = 0
        self.bill_text.delete('1.0', tk.END)  # Clear previous bill
        self.bill_text.insert(tk.END, "---- Bill ----\n")
        self.bill_text.insert(tk.END, f"{'Item':<20}{'Qty':<5}{'Price':<10}\n")

        # Process veg menu
        self.bill_text.insert(tk.END, "\n-- Veg Menu --\n")
        for item, details in self.veg_menu.items():
            quantity = self.veg_menu_entries[item].get()
            if quantity.isdigit() and int(quantity) > 0:
                quantity = int(quantity)
                self.veg_menu[item]['quantity'] = quantity
                price = quantity * details['price']
                total += price
                self.bill_text.insert(tk.END, f"{item:<20}{quantity:<5}{price:<10}\n")

        # Process non-veg menu
        self.bill_text.insert(tk.END, "\n-- Non-Veg Menu --\n")
        for item, details in self.non_veg_menu.items():
            quantity = self.non_veg_menu_entries[item].get()
            if quantity.isdigit() and int(quantity) > 0:
                quantity = int(quantity)
                self.non_veg_menu[item]['quantity'] = quantity
                price = quantity * details['price']
                total += price
                self.bill_text.insert(tk.END, f"{item:<20}{quantity:<5}{price:<10}\n")

        # Add extra charges
        if self.extra_var.get() == 1:
            self.bill_text.insert(tk.END, f"\nExtra Cheese: $2")
            total += 2

        self.bill_text.insert(tk.END, f"\nTotal: ${total}")
        self.bill_text.insert(tk.END, "\n------------------\n")

    def print_bill(self):
        bill = self.bill_text.get('1.0', tk.END)
        if bill.strip():
            # Simulate printing by displaying the bill in a message box
            messagebox.showinfo("Bill", bill)
        else:
            messagebox.showwarning("No Bill", "Please generate the bill first.")


if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantManagementSystem(root)
    root.mainloop()
