
def division(a,b):
    if b == 0:
        return "Error"
    return a/b


def factorial(a):
    k = 1
    for i in range(a):
        i = k * i
    return k

def diff(a,b):
    return a-b

def multiplication(a, b):
    return a*b

def sum(a,b): return a+b

def main():
    order = input("Введите операцию")
    a = int(input())
    b = int(input())
    if order =='+':
        print (sum (a,b))
    elif order =='-':
        print (diff (a,b))
    elif order =='*':
        print (multiplication (a,b))
    elif order =='/':
        print (division (a,b))
    elif order =='f':
        print (factorial (a,b))



