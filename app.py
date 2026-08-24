import tkinter as tk
from tkinter import ttk
import math
import matplotlib.pyplot as plt

class UltraCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("SCIENTIFIC CALCULATOR")
        self.root.geometry("420x720")
        self.root.configure(bg="#0f172a")

        self.expression = ""
        self.ans = 0
        self.history = []
        self.is_degree = True

        # ===== DISPLAY =====
        self.display = tk.Entry(root, font=("Consolas", 26),
                                bg="#020617", fg="#22d3ee",
                                bd=0, justify="right")
        self.display.pack(fill="both", ipadx=10, ipady=25, padx=10, pady=10)

        # ===== MODE =====
        self.mode_label = tk.Label(root, text="MODE: DEG",
                                   fg="#38bdf8", bg="#0f172a",
                                   font=("Arial", 10))
        self.mode_label.pack()

        # ===== HISTORY PANEL =====
        self.history_box = tk.Text(root, height=5,
                                  bg="#020617", fg="#94a3b8",
                                  font=("Consolas", 10))
        self.history_box.pack(fill="both", padx=10, pady=5)

        # ===== BUTTON FRAME =====
        frame = tk.Frame(root, bg="#0f172a")
        frame.pack()

        buttons = [
            ['C', 'DEL', '(', ')', '/'],
            ['7', '8', '9', '*', '√'],
            ['4', '5', '6', '-', 'x²'],
            ['1', '2', '3', '+', 'x^y'],
            ['0', '.', '=', '%', 'Ans'],
            ['sin', 'cos', 'tan', 'log', 'ln'],
            ['sin⁻¹', 'cos⁻¹', 'tan⁻¹', 'π', '!'],
            ['MODE', 'GRAPH', 'HIST', '', '']
        ]

        for i, row in enumerate(buttons):
            for j, btn in enumerate(row):
                if btn == "":
                    continue
                b = tk.Button(frame, text=btn,
                              width=6, height=2,
                              bg="#1e293b", fg="white",
                              activebackground="#334155",
                              relief="flat",
                              command=lambda b=btn: self.click(b))
                b.grid(row=i, column=j, padx=4, pady=4)

                # Hover effect
                b.bind("<Enter>", lambda e, x=b: x.config(bg="#334155"))
                b.bind("<Leave>", lambda e, x=b: x.config(bg="#1e293b"))

    # ===== SAFE EVALUATION =====
    def safe_eval(self, expr):
        try:
            expr = expr.replace('π', str(math.pi))
            return eval(expr)
        except:
            return "Error"

    # ===== GRAPH =====
    def plot_graph(self):
        try:
            x = list(range(-10, 10))
            y = [eval(self.expression.replace("x", str(i))) for i in x]

            plt.plot(x, y)
            plt.title("Graph of f(x)")
            plt.grid()
            plt.show()
        except:
            self.set_display("Graph Error")

    # ===== HISTORY =====
    def update_history(self, expr, result):
        entry = f"{expr} = {result}\n"
        self.history.append(entry)
        self.history_box.insert(tk.END, entry)

    # ===== MODE =====
    def toggle_mode(self):
        self.is_degree = not self.is_degree
        self.mode_label.config(
            text="MODE: DEG" if self.is_degree else "MODE: RAD"
        )

    # ===== CLICK =====
    def click(self, btn):
        try:
            if btn == 'C':
                self.expression = ""

            elif btn == 'DEL':
                self.expression = self.expression[:-1]

            elif btn == '=':
                result = self.safe_eval(self.expression)
                self.update_history(self.expression, result)
                self.ans = result
                self.expression = str(result)

            elif btn == 'Ans':
                self.expression += str(self.ans)

            elif btn == 'MODE':
                self.toggle_mode()
                return

            elif btn == 'GRAPH':
                self.plot_graph()
                return

            elif btn == 'HIST':
                return

            elif btn == '√':
                self.expression = str(math.sqrt(float(self.expression)))

            elif btn == 'x²':
                self.expression = str(float(self.expression) ** 2)

            elif btn == 'x^y':
                self.expression += '**'

            elif btn == 'sin':
                val = float(self.expression)
                if self.is_degree:
                    val = math.radians(val)
                self.expression = str(math.sin(val))

            elif btn == 'cos':
                val = float(self.expression)
                if self.is_degree:
                    val = math.radians(val)
                self.expression = str(math.cos(val))

            elif btn == 'tan':
                val = float(self.expression)
                if self.is_degree:
                    val = math.radians(val)
                self.expression = str(math.tan(val))

            elif btn == 'sin⁻¹':
                self.expression = str(math.degrees(math.asin(float(self.expression))))

            elif btn == 'cos⁻¹':
                self.expression = str(math.degrees(math.acos(float(self.expression))))

            elif btn == 'tan⁻¹':
                self.expression = str(math.degrees(math.atan(float(self.expression))))

            elif btn == 'log':
                self.expression = str(math.log10(float(self.expression)))

            elif btn == 'ln':
                self.expression = str(math.log(float(self.expression)))

            elif btn == '!':
                self.expression = str(math.factorial(int(float(self.expression))))

            else:
                self.expression += btn

            self.set_display(self.expression)

        except:
            self.expression = ""
            self.set_display("Error")

    def set_display(self, value):
        self.display.delete(0, tk.END)
        self.display.insert(0, value)


# ===== RUN =====
root = tk.Tk()
app = UltraCalculator(root)
root.mainloop()