# hesap_makinesi.py
import tkinter as tk
from tkinter import ttk, messagebox
import ast
import operator

# Güvenli değerlendirme: sadece belirlenen operator ve sayıları kabul eder
ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

def safe_eval(expr: str):
    """
    Basit ve güvenli bir ifade çözücü.
    İzin verilenler: sayılar, + - * /, parantez, unary +/-
    Hatalı veya izin verilmeyen öğe gelirse ValueError fırlatır.
    """
    try:
        node = ast.parse(expr, mode='eval').body
        return _eval_node(node)
    except Exception as e:
        raise ValueError("Geçersiz ifade") from e

def _eval_node(node):
    if isinstance(node, ast.BinOp):
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        op_type = type(node.op)
        if op_type in ALLOWED_OPERATORS:
            func = ALLOWED_OPERATORS[op_type]
            # Bölme sırasında ZeroDivisionError may occur naturally
            return func(left, right)
        raise ValueError("İzin verilmeyen işlem")
    elif isinstance(node, ast.UnaryOp):
        op_type = type(node.op)
        if op_type in ALLOWED_OPERATORS:
            operand = _eval_node(node.operand)
            return ALLOWED_OPERATORS[op_type](operand)
        raise ValueError("İzin verilmeyen unary işlem")
    elif isinstance(node, ast.Num):  # Python <3.8
        return node.n
    elif isinstance(node, ast.Constant):  # Python 3.8+
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Sadece sayılar izinli")
    elif isinstance(node, ast.Expr):
        return _eval_node(node.value)
    else:
        raise ValueError("İzin verilmeyen ifade öğesi")

# GUI
class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Basit Hesap Makinesi")
        self.resizable(False, False)
        self._build_ui()

    def _build_ui(self):
        # Display
        self.display_var = tk.StringVar()
        display = ttk.Entry(self, textvariable=self.display_var, justify="right", font=("Helvetica", 20), width=16)
        display.grid(row=0, column=0, columnspan=4, padx=8, pady=10, ipady=8)
        display.focus_set()

        # Buttons düzeni (row, col, text, cmd)
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("(", 4, 2), (")", 4, 3),
            ("C", 5, 0), ("⌫", 5, 1), ("=", 5, 2), ("+", 5, 3),
        ]

        for (txt, r, c) in buttons:
            action = (lambda char=txt: self.on_button(char))
            btn = ttk.Button(self, text=txt, command=action)
            btn.grid(row=r, column=c, sticky="nsew", padx=4, pady=4, ipadx=8, ipady=8)

        # Grid hücrelerini esnekleştir
        for i in range(6): self.rowconfigure(i, weight=1)
        for j in range(4): self.columnconfigure(j, weight=1)

        # Klavye kısayolları
        self.bind_all("<Return>", lambda e: self.calculate())
        self.bind_all("<BackSpace>", lambda e: self.backspace())
        for key in "0123456789.+-*/()":
            self.bind_all(key, lambda e, k=key: self._insert_char(k))

    def _insert_char(self, ch):
        # İmlecin olduğu yere eklemek yerine sona ekliyoruz (basit)
        current = self.display_var.get()
        self.display_var.set(current + ch)

    def on_button(self, char):
        if char == "C":
            self.display_var.set("")
        elif char == "⌫":
            self.backspace()
        elif char == "=":
            self.calculate()
        else:
            self._insert_char(char)

    def backspace(self):
        cur = self.display_var.get()
        self.display_var.set(cur[:-1])

    def calculate(self):
        expr = self.display_var.get().strip()
        if not expr:
            return
        try:
            result = safe_eval(expr)
            # Ondalıksa gereksiz .0 gösterimini kaldırmak için:
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.display_var.set(str(result))
        except ZeroDivisionError:
            messagebox.showerror("Hata", "Sıfıra bölme hatası")
        except ValueError:
            messagebox.showerror("Hata", "Geçersiz ifade")
        except Exception:
            messagebox.showerror("Hata", "Beklenmeyen hata")

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()


