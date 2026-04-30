# Implement numerical_second_derivative(f, x) using numerical_derivative called twice. Verify that the second derivative of x^3 at x=2 is 12.
def numerical_derivative(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

def numerical_second_derivative(f, x, h=1e-5):
    return (numerical_derivative(f, x + h, h) - numerical_derivative(f, x - h, h)) / (2 * h)

# Define the function f(x) = x^3
def f(x):
    return x ** 3

# Calculate the second derivative at x=2
x = 2
second_derivative_at_2 = numerical_second_derivative(f, x)
print(f"The second derivative of x^3 at x=2 is approximately: {second_derivative_at_2}")
# The expected value is 12, since the second derivative of x^3 is 6x, and at x=2, it should be 6*2 = 12.
