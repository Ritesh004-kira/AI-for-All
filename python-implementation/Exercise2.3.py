# Create a composition of three transformations (rotate 30 degrees, scale by [1.5, 0.8], shear with kx=0.3) and apply it to 8 points arranged in a circle. Print before and after coordinates. Compute the determinant of the composed matrix and verify it equals the product of the individual determinants.
import numpy as np
# Define the points arranged in a circle
theta = np.linspace(0, 2 * np.pi, 8, endpoint=False)
points = np.array([[np.cos(t), np.sin(t)] for t in theta])  
# Define transformation matrices
# Rotation by 30 degrees
rotation_angle = np.radians(30)
rotation_matrix = np.array([[np.cos(rotation_angle), -np.sin(rotation_angle)], 
                             [np.sin(rotation_angle), np.cos(rotation_angle)]])
# Scaling by [1.5, 0.8]
scaling_matrix = np.array([[1.5, 0], [0, 0.8]])
# Shearing with kx=0.3
shearing_matrix = np.array([[1, 0.3], [0, 1]])
# Compose the transformations
composed_matrix = shearing_matrix @ scaling_matrix @ rotation_matrix
# Apply the composed transformation to the points
transformed_points = points @ composed_matrix
print("Original points:\n", points)
print("Transformed points:\n", transformed_points)
# Compute the determinant of the composed matrix
det_composed = np.linalg.det(composed_matrix)
# Compute the product of the individual determinants
det_rotation = np.linalg.det(rotation_matrix)
det_scaling = np.linalg.det(scaling_matrix)
det_shearing = np.linalg.det(shearing_matrix)
product_of_dets = det_rotation * det_scaling * det_shearing
print(f"Determinant of composed matrix: {det_composed:.4f}")
print(f"Product of individual determinants: {product_of_dets:.4f}")
# Verify that the determinant of the composed matrix equals the product of the individual determinants
tolerance = 1e-10
determinants_match = abs(det_composed - product_of_dets) < tolerance
print("Determinants match:", determinants_match)
