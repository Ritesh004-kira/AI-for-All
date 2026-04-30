# Use gradient descent to find the minimum of f(x, y) = (x - 3)^2 + (y + 1)^2. Start from (0, 0). The answer should converge to (3, -1).
def f(x, y):
    return (x - 3) ** 2 + (y + 1) ** 2
def gradient_descent(learning_rate=0.1, max_iterations=1000):
    x, y = 0.0, 0.0  # Starting point
    for _ in range(max_iterations):
        # Calculate the gradients
        df_dx = 2 * (x - 3)
        df_dy = 2 * (y + 1)
        
        # Update the variables
        x -= learning_rate * df_dx
        y -= learning_rate * df_dy
        
    return x, y 

result = gradient_descent()
print(f"Minimum found at: {result}")
