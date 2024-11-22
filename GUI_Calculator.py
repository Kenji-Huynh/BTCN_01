import tkinter as tk
from tkinter import ttk

class SimpleCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Calculator")
        self.geometry("600x600")
        self.configure(bg="#f0f0f0")
        self.create_widgets()

    def create_widgets(self):
        # Display field
        self.display = ttk.Entry(self, font=("Helvetica", 20), justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Calculator buttons
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        row = 1
        col = 0
        for button in buttons:
            if button == "=":
                ttk.Button(self, text=button, command=self.evaluate, style="Accent.TButton").grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            else:
                ttk.Button(self, text=button, command=lambda x=button: self.add_to_display(x), style="TButton").grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Clear button
        ttk.Button(self, text="C", command=self.clear_display, style="Accent.TButton").grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

    def add_to_display(self, value):
        self.display.insert("end", value)

    def clear_display(self):
        self.display.delete(0, "end")

    def evaluate(self):
        try:
            result = str(eval(self.display.get()))
            self.display.delete(0, "end")
            self.display.insert(0, result)
        except:
            self.display.delete(0, "end")
            self.display.insert(0, "Error")

if __name__ == "__main__":
    app = SimpleCalculator()
    app.mainloop()