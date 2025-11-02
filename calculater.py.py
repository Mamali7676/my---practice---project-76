
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else "Division by zero!"

print("ماشین حساب پایتونی 📱")
a = float(input("عدد اول: "))
b = float(input("عدد دوم: "))
op = input("عملگر (+, -, *, /): ")

if op == "+": print(add(a, b))
elif op == "-": print(sub(a, b))
elif op == "*": print(mul(a, b))
elif op == "/": print(div(a, b))
else: print("عملگر اشتباهه 😅")