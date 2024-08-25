import tkinter as tk

class Calculator(tk.Tk):
    def _init_(self):
        super()._init_()
        self.title("Calculadora")
        self.geometry("300x400")
        
        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Display
        display = tk.Entry(self, textvariable=self.result_var, font=("Arial", 24), bd=10, relief="ridge", justify="right")
        display.grid(row=0, column=0, columnspan=4)
        
        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        
        row_val = 1
        col_val = 0
        
        for button in buttons:
            tk.Button(self, text=button, font=("Arial", 18), width=5, height=2, command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, button):
        current = self.result_var.get()
        
        if button == 'C':
            self.result_var.set("")
        elif button == '=':
            try:
                result = eval(current)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            self.result_var.set(current + button)

if _name_ == "_main_":
    app = Calculator()
    app.mainloop()