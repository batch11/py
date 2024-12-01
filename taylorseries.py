import math

# Function to calculate sin(x) using Taylor series
def sin(x, n):
    x = math.radians(x)  # Convert angle to radians
    result = 0
    
    for i in range(n):
        # Calculate the term: ((-1)^i * x^(2i+1)) / (2i+1)!
        term = ((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
        result += term
    
    return result

# Input: angle in degrees and number of terms
angle = float(input("Enter the angle in degrees: "))
terms = int(input("Enter the number of terms: "))

# Calculate and display the result
approx_sin = sin(angle, terms)
print(f"sin({angle}) ≈ {approx_sin}")
