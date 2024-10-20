from fastapi import FastAPI, HTTPException
from calculation import plus, minus, multiply, divide

app = FastAPI()

@app.get("/calculate")
async def calculate_api(calculation: str, a: float, b: float):
    try:
        if calculation == '+':
            result = plus(a, b) 
        elif calculation == '-':
            result = minus(a, b) 
        elif calculation == '*':
            result = multiply(a, b)  
        elif calculation == '/':
            result = divide(a, b)
        elif calculation == '^':
            result = power(a, b)
        elif calculation == 'sqrt':
            result = square_root(a)
        else:
            raise ValueError("Invalid calculation type.")

        return {f"{a} {calculation} {b if b is not None else ''}": result}
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
