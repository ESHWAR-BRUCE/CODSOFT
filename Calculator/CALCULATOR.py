import tkinter as tk

class UniqueCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        
        self.expression = ""
        self.input_text = tk.StringVar()

        # Configure the main frame
        self.frame = tk.Frame(master, bg="#ffffff")
        self.frame.pack(padx=10, pady=10)

        # Entry widget
        self.entry = tk.Entry(self.frame, textvariable=self.input_text, font=('Arial', 24), bd=8, insertwidth=2, width=14, borderwidth=4)
        self.entry.grid(row=0, column=0, columnspan=4)

        # Button layout with unique colors and styles
        buttons = [
            ('7', '#8c8a88'), ('8', '#8c8a88'), ('9', '#8c8a88'), ('/', '#ffffff'),
            ('4', '#8c8a88'), ('5', '#8c8a88'), ('6', '#8c8a88'), ('*', '#ffffff'),
            ('1', '#8c8a88'), ('2', '#8c8a88'), ('3', '#8c8a88'), ('-', '#ffffff'),
            ('C', '#bbb8b6'), ('0', '#8c8a88'), ('=', '#007619'), ('+', '#ffffff')
        ]

        row_val = 1
        col_val = 0

        for (text, color) in buttons:
            tk.Button(self.frame, text=text, padx=20, pady=20, font=('Arial', 20),
                      bg=color, command=lambda b=text: self.on_button_click(b)).grid(row=row_val, column=col_val, sticky="nsew")
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Make buttons stretchable
        for i in range(4):
            self.frame.grid_columnconfigure(i, weight=1)

    def on_button_click(self, button):
        if button == 'C':
            self.expression = ""
        elif button == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "Error"
        else:
            self.expression += button
        self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = UniqueCalculator(root)
    root.mainloop()
