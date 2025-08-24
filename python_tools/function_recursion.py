# functions_recursion.py

def is_even(n: int) -> bool:
    return n % 2 == 0

def greet(name: str = "student") -> str:
    return f"Hello, {name}! 👋"

# --- Recursion examples ---
def factorial(n: int) -> int:
    """n! = n * (n-1)!, factorial(0) = 1"""
    if n < 0:
        raise ValueError("factorial undefined for negative numbers")
    return 1 if n in (0, 1) else n * factorial(n - 1)

def fibonacci(n: int) -> int:
    """0, 1, 1, 2, 3, 5, ..."""
    if n < 0:
        raise ValueError("fibonacci undefined for negative numbers")
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    # Functions w/ and w/o arguments
    print(greet())
    print(greet("Dan"))
    for x in range(5):
        print(f"{x} even? {is_even(x)}")

    # Recursion demos
    print("factorial(5) =", factorial(5))
    print("fibonacci(10) =", fibonacci(10))

if __name__ == "__main__":
    main()
