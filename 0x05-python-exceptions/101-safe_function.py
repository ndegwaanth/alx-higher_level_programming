#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print(f"Exception: {e}", file=sys.stderr)
        return None

# Example usage:
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

result = safe_function(divide, 10, 2)
print("Result:", result)

result = safe_function(divide, 10, 0)
print("Result:", result)
