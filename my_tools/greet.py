from langchain import tool

@tool
def say_hello(name: str)-> str:
    """Useful for greeting a user"""
    print("Greeting tool was called.")
    return f"Hello {name}, I hope you are well today"
