# Function to return the larger of two values or None if they are equal
def maximum(a, b):
    if a == b:
        return None
    else:
        return a if a > b else b

# Test cases
print(maximum(15, 20))  # Second argument bigger
print(maximum(100, 50)) # First argument bigger
print(maximum(-5, -5))  # Both arguments equal
