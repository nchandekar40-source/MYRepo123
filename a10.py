def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

num_terms = 8
print(f"Fibonacci sequence up to {num_terms} terms:")
fibonacci(num_terms)
print() # For a new line after the sequence