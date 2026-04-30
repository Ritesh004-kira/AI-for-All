# Add momentum to the gradient descent loop: maintain a velocity vector that accumulates past gradients. Compare convergence speed with and without momentum on f(x) = x^4 - 3x^2.

def f(x):
    return x ** 4 - 3 * x ** 2
def gradient_descent_with_momentum(learning_rate=0.01, momentum=0.9, max_iterations=1000):
    x = 0.0  # Starting point
    velocity = 0.0  # Initialize velocity
    for _ in range(max_iterations):
        # Calculate the gradient
        df_dx = 4 * x ** 3 - 6 * x
        
        # Update velocity and position
        velocity = momentum * velocity + learning_rate * df_dx
        x -= velocity
        
    return x    
def gradient_descent_without_momentum(learning_rate=0.01, max_iterations=1000):
    x = 0.0  # Starting point
    for _ in range(max_iterations):
        # Calculate the gradient
        df_dx = 4 * x ** 3 - 6 * x
        
        # Update position
        x -= learning_rate * df_dx
        
    return x
result_with_momentum = gradient_descent_with_momentum()
result_without_momentum = gradient_descent_without_momentum()
print(f"Minimum with momentum found at: {result_with_momentum}")
print(f"Minimum without momentum found at: {result_without_momentum}")
