from langchain.tools import tool

@tool
def add(a: float,b: float)-> str:
    """Useful for basic arithmetic addition with numbers"""
    return f"The sum of {a} and {b} is {a+b}"

@tool
def sub(a: float,b: float) -> str:
    """"Useful basic arithmetic subtraction with numbers"""
    return f"The subraction of {a} and {b} is {a-b}"

@tool
def multiplication(a: float,b: float) -> str:
    """"Useful basic arithmetic multiplication with numbers"""
    return f"The multiplication of {a} and {b} is {a*b}"

@tool
def division(a: float,b: float) -> str:
    """"Useful basic arithmetic division with numbers"""
    if b==0:
        return f"cannot divide with zero"
    return f"The division of {a} and {b} is {a/b}"