a = input()

plus = []
minus = []
div = []
multi = []

while a != "":
    b = input()
    op = input()
    c = "Oops. Something went wrong."
    
    if op == "+":
        c = a + op + b + "=" + str(int(a) + int(b))
        plus.append(c)
    elif op == "-":
        c = a + op + b + "=" + str(int(a) - int(b))
        minus.append(c)
    elif op == "/":
        c = a + op + b + "=" + str(int(a) / int(b))
        div.append(c)
    elif op == "*":
        c = a + op + b + "=" + str(int(a) * int(b))
        multi.append(c)
        
    print(c)
    print("+", plus)
    print("-", minus)
    print("/", div)
    print("*", multi)
    
    a = input()

