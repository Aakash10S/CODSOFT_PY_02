import tkinter as tk
from tkinter import messagebox

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x300")

        # Input fields
        self.num1_label = tk.Label(self.root, text="Enter First Number:", font=("Arial", 12))
        self.num1_label.pack(pady=5)
        self.num1_entry = tk.Entry(self.root, font=("Arial", 12))
        self.num1_entry.pack(pady=5)

        self.num2_label = tk.Label(self.root, text="Enter Second Number:", font=("Arial", 12))
        self.num2_label.pack(pady=5)
        self.num2_entry = tk.Entry(self.root, font=("Arial", 12))
        self.num2_entry.pack(pady=5)

        # Operation choices
        self.operation_label = tk.Label(self.root, text="Choose Operation:", font=("Arial", 12))
        self.operation_label.pack(pady=5)

        self.operation_var = tk.StringVar(value="+")
        self.operations = {"+": "Add", "-": "Subtract", "*": "Multiply", "/": "Divide"}

        for op, desc in self.operations.items():
            tk.Radiobutton(self.root, text=desc, variable=self.operation_var, value=op, font=("Arial", 12)).pack(anchor=tk.W)

        # Calculate button
        self.calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate, font=("Arial", 12))
        self.calculate_button.pack(pady=10)

        # Result display
        self.result_label = tk.Label(self.root, text="Result: ", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get().strip())
            num2 = float(self.num2_entry.get().strip())
            operation = self.operation_var.get()

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 != 0:
                    result = num1 / num2
                else:
                    messagebox.showerror("Error", "Cannot divide by zero!")
                    return
            else:
                messagebox.showerror("Error", "Invalid operation!")
                return

            self.result_label.config(text=f"Result: {result:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers!")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleCalculator(root)
    root.mainloop()
