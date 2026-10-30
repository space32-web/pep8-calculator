import math
def Add(a,b):
    return a+b
def Subtract(a,b): return a-b
def Multiply(a,b):
  return a*b
def Divide(a,b):
    if b==0 : raise ValueError("Деление на ноль")
    return a/b
OPERATIONS={'+':Add,'-':Subtract,'*':Multiply,'/':Divide}
def calculate(expression):
    left,operator,right=expression.split()
    return OPERATIONS[operator](float(left),float(right))
if __name__=="__main__":
    print(calculate(input("Выражение (например, 2 + 3): ")))
