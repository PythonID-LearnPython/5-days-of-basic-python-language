# Day 4: Functions - Tuple

def calc(a: int, b: int):
    return a + b, a - b, a * b

sum_result, difference, product = calc(10, 5)
print("Sum:", sum_result, "Difference:", difference, "Product:", product)