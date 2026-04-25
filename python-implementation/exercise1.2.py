# Create a 2D scaling matrix that doubles the x-coordinate and triples the y-coordinate, then apply it to the vector [1, 1]
import numpy as np  
# Define the scaling matrix
scaling_matrix = np.array([[2, 0], [0, 3]])
# Define the vector
vector = np.array([1, 1])
# Apply the scaling transformation
scaled_vector = np.dot(scaling_matrix, vector)
print(f"Scaled vector: {scaled_vector}")
