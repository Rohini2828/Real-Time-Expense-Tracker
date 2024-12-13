import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

expenses = []


def add_expense():
    category = category_entry.get()
    amount = amount_entry.get()
    date = date_entry.get()

    if not category or not amount or not date:
        messagebox.showerror("Input Error", "All fields are required!")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Input Error", "Amount must be a number!")
        return

    expenses.append({"category": category, "amount": amount, "date": date})
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)

    update_expense_display()


def update_expense_display():
    expense_list.delete(1.0, tk.END)  
    for expense in expenses:
        expense_list.insert(tk.END, f"Category: {expense['category']}, Amount: ${expense['amount']:.2f}, Date: {expense['date']}\n")

def show_chart():
    if not expenses:
        messagebox.showerror("Error", "No expenses to show!")
        return

    categories = [expense["category"] for expense in expenses]
    amounts = [expense["amount"] for expense in expenses]

    plt.bar(categories, amounts, color="skyblue")
    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.show()


root = tk.Tk()
root.title("Expense Tracker")
root.geometry("500x400")  

tk.Label(root, text="Category:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
category_entry = tk.Entry(root)
category_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Amount:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
amount_entry = tk.Entry(root)
amount_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
date_entry = tk.Entry(root)
date_entry.grid(row=2, column=1, padx=10, pady=5)

add_expense_btn = tk.Button(root, text="Add Expense", command=add_expense)
add_expense_btn.grid(row=3, column=0, columnspan=2, pady=10)

show_chart_btn = tk.Button(root, text="Show Chart", command=show_chart)
show_chart_btn.grid(row=4, column=0, columnspan=2, pady=10)

expense_list = tk.Text(root, height=10, width=50)
expense_list.grid(row=5, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()
