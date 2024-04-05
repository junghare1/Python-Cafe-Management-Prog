# # import tkinter as tk
# # from tkinter import ttk
# # root = tk.Tk()
# # root.title("BLA BLA CAFE")
# # root.configure(bg="#abd1ff")
# # # root.resizable(height=FALSE, width=FALSE)


# # food_items = {"Pizza": ["Cheese Pizza", "Veg Pizza", "Non-Veg Pizza"],
# #     "Burger": ["Cheese Burger", "Veg Burger", "Non-Veg Burger"],
# #     "Shake": ["Orio Shake", "Mango Shake", "Chocolate Shake"],
# #     "Pasta": ["Simple Pasta", "White Souce Pasta", "Pink Pasta"],
# #     "Maggie": ["Plain Maggi", "Masala Maggi", "Peri Peri Maggi"]}

# # def calculate_total():
# #     total = 0

# #     for food_item, combo in combos.items():
# #         selected_item = combo.get()
# #         if selected_item:
# #             quantity = int(entry_quantities[food_item].get())
# #             price = prices[food_item][selected_item]
# #             total += price * quantity

# #     label_total.config(text=f"Total Amount: Rs {total}")

# # def generate_bill():
# #     bill_text = "Cafe Bill\n\n"

# #     for food_item, combo in combos.items():
# #         selected_item = combo.get()
# #         if selected_item:
# #             quantity = int(entry_quantities[food_item].get())
# #             price = prices[food_item][selected_item]
# #             total = price * quantity
# #             bill_text += f"Item: {selected_item}\nQuantity: {quantity}\nTotal Amount: Rs {total}\n\n"

# #     label_total.config(text="Total Amount: Rs 0")
# #     text_bill.delete("1.0", tk.END)
# #     if bill_text == "Cafe Bill\n\n":
# #         bill_text = "No items selected!"
# #     else:
# #         total_amount = sum([prices[food_item][combo.get()] * int(entry_quantities[food_item].get()) for food_item, combo in combos.items() if combo.get()])
# #         bill_text += f"Total Amount: Rs {total_amount}\n\nThank you for dining with us!"

# #     text_bill.insert(tk.END, bill_text)



# # combos = {}
# # entry_quantities = {}
# # prices = {
# #     "Pizza": {
# #         "Cheese Pizza": 180,
# #         "Veg Pizza": 150,
# #         "Non-Veg Pizza": 200
# #     },
# #     "Burger": {
# #         "Cheese Burger": 80,
# #         "Veg Burger": 60,
# #         "Non-Veg Burger": 100
# #     },
# #     "Shake": {
# #         "Orio Shake": 80,
# #         "Mango Shake": 100,
# #         "Chocolate Shake": 80
# #     },
# #     "Pasta": {
# #         "Simple Pasta": 90,
# #         "White Souce Pasta": 120,
# #         "Pink Pasta": 150
# #     },
# #     "Maggie": {
# #         "Plain Maggi": 60,
# #         "Masala Maggi": 90,
# #         "Peri Peri Maggi": 120
# #     }
# # }

# # row = 0
# # for food_item, items in food_items.items():
# #     label_item = tk.Label(root, text=food_item + ":", bg="#e54b22")
# #     label_item.grid(row=row, column=0, sticky="w")

# #     combo = ttk.Combobox(root, values=items)
# #     combo.grid(row=row, column=1)

# #     label_quantity = tk.Label(root, text="Quantity:", bg="#e54b22")
# #     label_quantity.grid(row=row, column=2, padx=(10, 0))

# #     entry_quantity = tk.Entry(root)
# #     entry_quantity.grid(row=row, column=3)
# #     entry_quantities[food_item] = entry_quantity

# #     combos[food_item] = combo

# #     row += 1

# # # Calculate Total Button
# # btn_calculate = tk.Button(root, text="Calculate Total", command=calculate_total)
# # btn_calculate.grid(row=row, column=0, pady=(10, 0), columnspan=2)

# # # Total Amount
# # label_total = tk.Label(root, text="Total Amount: Rs 0", bg="#e54b22")
# # label_total.grid(row=row, column=2, columnspan=2, pady=(10, 0))

# # row += 1

# # # Generate Bill Button
# # btn_generate_bill = tk.Button(root, text="Generate Bill", command=generate_bill)
# # btn_generate_bill.grid(row=row, column=0, pady=(10, 0), columnspan=2)

# # row += 1

# # # Bill Text
# # text_bill = tk.Text(root, height=10, width=30)
# # text_bill.grid(row=row, column=0, columnspan=4, pady=(10, 0))

# # root.mainloop()






# import tkinter as tk
# from tkinter import ttk
# import sqlite3

# root = tk.Tk()
# root.title("BLA BLA CAFE")
# root.configure(bg="#abd1ff")

# # Create or connect to a SQLite3 database
# conn = sqlite3.connect('cafe.db')
# c = conn.cursor()

# # Create table if not exists
# c.execute('''CREATE TABLE IF NOT EXISTS bills
#              (id INTEGER PRIMARY KEY AUTOINCREMENT, item TEXT, quantity INTEGER, total INTEGER)''')
# conn.commit()


# food_items = {"Pizza": ["Cheese Pizza", "Veg Pizza", "Non-Veg Pizza"],
#               "Burger": ["Cheese Burger", "Veg Burger", "Non-Veg Burger"],
#               "Shake": ["Orio Shake", "Mango Shake", "Chocolate Shake"],
#               "Pasta": ["Simple Pasta", "White Souce Pasta", "Pink Pasta"],
#               "Maggie": ["Plain Maggi", "Masala Maggi", "Peri Peri Maggi"]}


# def calculate_total():
#     total = 0
#     for food_item, combo in combos.items():
#         selected_item = combo.get()
#         if selected_item:
#             quantity = int(entry_quantities[food_item].get())
#             price = prices[food_item][selected_item]
#             total += price * quantity
#     label_total.config(text=f"Total Amount: Rs {total}")


# def generate_bill():
#     bill_text = "Cafe Bill\n\n"
#     for food_item, combo in combos.items():
#         selected_item = combo.get()
#         if selected_item:
#             quantity = int(entry_quantities[food_item].get())
#             price = prices[food_item][selected_item]
#             total = price * quantity
#             # Insert bill information into the database
#             c.execute("INSERT INTO bills (item, quantity, total) VALUES (?, ?, ?)",
#                       (selected_item, quantity, total))
#             conn.commit()
#             bill_text += f"Item: {selected_item}\nQuantity: {quantity}\nTotal Amount: Rs {total}\n\n"

#     label_total.config(text="Total Amount: Rs 0")
#     text_bill.delete("1.0", tk.END)
#     if bill_text == "Cafe Bill\n\n":
#         bill_text = "No items selected!"
#     else:
#         total_amount = sum([prices[food_item][combo.get()] * int(entry_quantities[food_item].get()) for food_item, combo in combos.items() if combo.get()])
#         bill_text += f"Total Amount: Rs {total_amount}\n\nThank you for dining with us!"
#     text_bill.insert(tk.END, bill_text)


# def show_bills():
#     bill_window = tk.Toplevel(root)
#     bill_window.title("Previous Bills")

#     scrollbar = tk.Scrollbar(bill_window)
#     scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

#     listbox = tk.Listbox(bill_window, yscrollcommand=scrollbar.set)
#     listbox.pack(fill=tk.BOTH, expand=True)

#     for row in c.execute("SELECT * FROM bills"):
#         listbox.insert(tk.END, f"ID: {row[0]}, Item: {row[1]}, Quantity: {row[2]}, Total Amount: Rs {row[3]}")

#     scrollbar.config(command=listbox.yview)


# combos = {}
# entry_quantities = {}
# prices = {
#     "Pizza": {
#         "Cheese Pizza": 180,
#         "Veg Pizza": 150,
#         "Non-Veg Pizza": 200
#     },
#     "Burger": {
#         "Cheese Burger": 80,
#         "Veg Burger": 60,
#         "Non-Veg Burger": 100
#     },
#     "Shake": {
#         "Orio Shake": 80,
#         "Mango Shake": 100,
#         "Chocolate Shake": 80
#     },
#     "Pasta": {
#         "Simple Pasta": 90,
#         "White Souce Pasta": 120,
#         "Pink Pasta": 150
#     },
#     "Maggie": {
#         "Plain Maggi": 60,
#         "Masala Maggi": 90,
#         "Peri Peri Maggi": 120
#     }
# }

# row = 0
# for food_item, items in food_items.items():
#     label_item = tk.Label(root, text=food_item + ":", bg="#e54b22")
#     label_item.grid(row=row, column=0, sticky="w")

#     combo = ttk.Combobox(root, values=items)
#     combo.grid(row=row, column=1)

#     label_quantity = tk.Label(root, text="Quantity:", bg="#e54b22")
#     label_quantity.grid(row=row, column=2, padx=(10, 0))

#     entry_quantity = tk.Entry(root)
#     entry_quantity.grid(row=row, column=3)
#     entry_quantities[food_item] = entry_quantity

#     combos[food_item] = combo

#     row += 1

# # Calculate Total Button
# btn_calculate = tk.Button(root, text="Calculate Total", command=calculate_total)
# btn_calculate.grid(row=row, column=0, pady=(10, 0), columnspan=2)

# # Total Amount
# label_total = tk.Label(root, text="Total Amount: Rs 0", bg="#e54b22")
# label_total.grid(row=row, column=2, columnspan=2, pady=(10, 0))

# row += 1

# # Generate Bill Button
# btn_generate_bill = tk.Button(root, text="Generate Bill", command=generate_bill)
# btn_generate_bill.grid(row=row, column=0, pady=(10, 0), columnspan=2)

# row += 1

# # Show Bills Button
# btn_show_bills = tk.Button(root, text="Show Previous Bills", command=show_bills)
# btn_show_bills.grid(row=row, column=2, pady=(10, 0), columnspan=2)

# row += 1

# # Bill Text
# text_bill = tk.Text(root, height=10, width=30)
# text_bill.grid(row=row, column=0, columnspan=4, pady=(10, 0))

# root.mainloop()

# # Close the database connection when the GUI is closed
# conn.close()



import tkinter as tk
from tkinter import ttk
import sqlite3

root = tk.Tk()
root.title("BLA BLA CAFE")
root.configure(bg="#abd1ff")

# Create or connect to a SQLite3 database
conn = sqlite3.connect('cafe.db')
c = conn.cursor()

# Create table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS bills
             (id INTEGER PRIMARY KEY AUTOINCREMENT, item TEXT, quantity INTEGER, total INTEGER)''')
conn.commit()


food_items = {"Pizza": ["Cheese Pizza", "Veg Pizza", "Non-Veg Pizza"],
              "Burger": ["Cheese Burger", "Veg Burger", "Non-Veg Burger"],
              "Shake": ["Orio Shake", "Mango Shake", "Chocolate Shake"],
              "Pasta": ["Simple Pasta", "White Souce Pasta", "Pink Pasta"],
              "Maggie": ["Plain Maggi", "Masala Maggi", "Peri Peri Maggi"]}


def calculate_total():
    total = 0
    for food_item, combo in combos.items():
        selected_item = combo.get()
        if selected_item:
            quantity = int(entry_quantities[food_item].get())
            price = prices[food_item][selected_item]
            total += price * quantity
    label_total.config(text=f"Total Amount: Rs {total}")


def generate_bill():
    bill_text = "Cafe Bill\n\n"
    for food_item, combo in combos.items():
        selected_item = combo.get()
        if selected_item:
            quantity = int(entry_quantities[food_item].get())
            price = prices[food_item][selected_item]
            total = price * quantity
            # Insert bill information into the database
            c.execute("INSERT INTO bills (item, quantity, total) VALUES (?, ?, ?)",
                      (selected_item, quantity, total))
            conn.commit()
            bill_text += f"Item: {selected_item}\nQuantity: {quantity}\nTotal Amount: Rs {total}\n\n"

    label_total.config(text="Total Amount: Rs 0")
    text_bill.delete("1.0", tk.END)
    if bill_text == "Cafe Bill\n\n":
        bill_text = "No items selected!"
    else:
        total_amount = sum([prices[food_item][combo.get()] * int(entry_quantities[food_item].get()) for food_item, combo in combos.items() if combo.get()])
        bill_text += f"Total Amount: Rs {total_amount}\n\nThank you for dining with us!"
    text_bill.insert(tk.END, bill_text)


def show_bills():
    bill_window = tk.Toplevel(root)
    bill_window.title("Previous Bills")

    scrollbar = tk.Scrollbar(bill_window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox = tk.Listbox(bill_window, yscrollcommand=scrollbar.set)
    listbox.pack(fill=tk.BOTH, expand=True)

    for row in c.execute("SELECT * FROM bills"):
        listbox.insert(tk.END, f"ID: {row[0]}, Item: {row[1]}, Quantity: {row[2]}, Total Amount: Rs {row[3]}")

    scrollbar.config(command=listbox.yview)


combos = {}
entry_quantities = {}
prices = {
    "Pizza": {
        "Cheese Pizza": 180,
        "Veg Pizza": 150,
        "Non-Veg Pizza": 200
    },
    "Burger": {
        "Cheese Burger": 80,
        "Veg Burger": 60,
        "Non-Veg Burger": 100
    },
    "Shake": {
        "Orio Shake": 80,
        "Mango Shake": 100,
        "Chocolate Shake": 80
    },
    "Pasta": {
        "Simple Pasta": 90,
        "White Souce Pasta": 120,
        "Pink Pasta": 150
    },
    "Maggie": {
        "Plain Maggi": 60,
        "Masala Maggi": 90,
        "Peri Peri Maggi": 120
    }
}

row = 0
for food_item, items in food_items.items():
    label_item = tk.Label(root, text=food_item + ":", bg="#e54b22")
    label_item.grid(row=row, column=0, sticky="w")

    combo = ttk.Combobox(root, values=items, style='ComboStyle.TCombobox')
    combo.grid(row=row, column=1)

    label_quantity = tk.Label(root, text="Quantity:", bg="#e54b22")
    label_quantity.grid(row=row, column=2, padx=(10, 0))

    entry_quantity = tk.Entry(root)
    entry_quantity.grid(row=row, column=3)
    entry_quantities[food_item] = entry_quantity

    combos[food_item] = combo

    row += 1

# Calculate Total Button
btn_calculate = tk.Button(root, text="Calculate Total", command=calculate_total)
btn_calculate.grid(row=row, column=0, pady=(10, 0), columnspan=2)

# Total Amount
label_total = tk.Label(root, text="Total Amount: Rs 0", bg="#e54b22")
label_total.grid(row=row, column=2, columnspan=2, pady=(10, 0))

row += 1

# Generate Bill Button
btn_generate_bill = tk.Button(root, text="Generate Bill", command=generate_bill)
btn_generate_bill.grid(row=row, column=0, pady=(10, 0), columnspan=2)

row += 1

# Show Bills Button
btn_show_bills = tk.Button(root, text="Show Previous Bills", command=show_bills)
btn_show_bills.grid(row=row, column=2, pady=(10, 0), columnspan=2)

row += 1

# Bill Text
text_bill = tk.Text(root, height=10, width=30)
text_bill.grid(row=row, column=0, columnspan=4, pady=(10, 0))

# Style for 3D combo box
style = ttk.Style()
style.theme_create('ComboStyle', parent='alt', settings={
    'TCombobox': {'configure': {'selectbackground': 'orange', 'fieldbackground': '#FFF', 'background': 'red'}}})

style.theme_use('ComboStyle')

root.mainloop()

# Close the database connection when the GUI is closed
conn.close()
