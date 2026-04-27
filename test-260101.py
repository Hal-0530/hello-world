import tkinter as tk
from tkinter import font
import random

class ArithmeticGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("四則演算ゲーム")
        self.root.geometry("400x300")
        self.root.configure(bg="white")
        
        # ゲームの状態
        self.left_num = random.randint(1, 9)
        self.right_num = random.randint(1, 9)
        self.operator = random.choice(['+', '-', '*', '/'])
        self.result = None
        self.calculate_result()
        
        # フォント設定
        self.large_font = font.Font(family="Arial", size=36, weight="bold")
        self.medium_font = font.Font(family="Arial", size=24)
        self.normal_font = font.Font(family="Arial", size=14)
        
        # フレーム構成
        # 上部：判定表示（丸またはバツ）
        self.judge_frame = tk.Frame(root, bg="white", height=50)
        self.judge_frame.pack(fill=tk.X, padx=20, pady=10)
        self.judge_label = tk.Label(self.judge_frame, text="", font=self.large_font, bg="white", fg="blue")
        self.judge_label.pack(expand=True, anchor="center")
        
        # 中央：四則演算式
        self.expression_frame = tk.Frame(root, bg="white", height=100)
        self.expression_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # 中央左：数字
        self.left_label = tk.Label(self.expression_frame, text=str(self.left_num), font=self.large_font, bg="white")
        self.left_label.pack(side=tk.LEFT, padx=10, anchor="center")
        
        # 中央：演算記号
        self.operator_label = tk.Label(self.expression_frame, text=self.operator, font=self.large_font, bg="white")
        self.operator_label.pack(side=tk.LEFT, padx=10, anchor="center")
        
        # 中央右：数字
        self.right_label = tk.Label(self.expression_frame, text=str(self.right_num), font=self.large_font, bg="white")
        self.right_label.pack(side=tk.LEFT, padx=10, anchor="center")
        
        # 下部：入力フレーム
        self.input_frame = tk.Frame(root, bg="white")
        self.input_frame.pack(fill=tk.X, padx=20, pady=10)
        
        tk.Label(self.input_frame, text="答え:", font=self.normal_font, bg="white").pack(side=tk.LEFT, padx=5, expand=True, anchor="center")
        
        self.entry = tk.Entry(self.input_frame, font=self.normal_font, width=10)
        self.entry.pack(side=tk.LEFT, padx=5, expand=True, anchor="center")
        self.entry.bind("<Return>", lambda event: self.check_answer())
        
        self.check_button = tk.Button(self.input_frame, text="送信", font=self.normal_font, command=self.check_answer)
        self.check_button.pack(side=tk.LEFT, padx=5, expand=True, anchor="center")
        
        self.entry.focus()
    
    def calculate_result(self):
        """計算結果を求める"""
        if self.operator == '+':
            self.result = self.left_num + self.right_num
        elif self.operator == '-':
            self.result = self.left_num - self.right_num
        elif self.operator == '*':
            self.result = self.left_num * self.right_num
        elif self.operator == '/':
            self.result = self.left_num / self.right_num
    
    def check_answer(self):
        """入力された答えを確認"""
        try:
            user_answer = float(self.entry.get())
            
            # 判定
            if abs(user_answer - self.result) < 0.0001:  # 浮動小数点誤差を考慮
                self.judge_label.config(text="○", fg="blue")
            else:
                self.judge_label.config(text="×", fg="red")
            
            # 次の問題へ（2秒後）
            self.root.after(2000, self.next_question)
        except ValueError:
            self.judge_label.config(text="数字を入力してください", fg="red")
            self.root.after(1500, lambda: self.judge_label.config(text=""))
    
    def next_question(self):
        """次の問題を生成"""
        self.left_num = random.randint(1, 9)
        self.right_num = random.randint(1, 9)
        self.operator = random.choice(['+', '-', '*', '/'])
        self.calculate_result()
        
        # 表示を更新
        self.left_label.config(text=str(self.left_num))
        self.operator_label.config(text=self.operator)
        self.right_label.config(text=str(self.right_num))
        self.judge_label.config(text="")
        self.entry.delete(0, tk.END)
        self.entry.focus()

if __name__ == "__main__":
    root = tk.Tk()
    app = ArithmeticGameApp(root)
    root.mainloop()
