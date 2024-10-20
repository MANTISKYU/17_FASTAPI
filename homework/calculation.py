def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("0으로는 나눌 수 없습니다")
    return a / b
    
def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("음수를 사용할 수 없습니다")
    return a ** 0.5 
