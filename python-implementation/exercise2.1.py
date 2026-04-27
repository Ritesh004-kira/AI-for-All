# Apply rotation, scaling, and shearing to a unit square (corners at [0,0], [1,0], [1,1], [0,1]). Print the transformed corners for each. Verify that rotation preserves distances between corners.
import numpy as np
# Define the corners of the unit square
corners = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
# Define transformation matrices
# Rotation by 45 degrees
theta = np.radians(45)
rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
# Scaling by a factor of 2
scaling_matrix = np.array([[2, 0], [0, 2]])
# Shearing with a factor of 1
shearing_matrix = np.array([[1, 1], [0, 1]])
# Apply transformations
rotated_corners = corners @ rotation_matrix
scaled_corners = corners @ scaling_matrix
sheared_corners = corners @ shearing_matrix
print("Rotated corners:\n", rotated_corners)
print("Scaled corners:\n", scaled_corners)
print("Sheared corners:\n", sheared_corners)
# Verify that rotation preserves distances between corners
def distance(p1, p2):
    return np.linalg.norm(p1 - p2)

# Calculate distances for the original square
original_distances = []
for i in range(4):
    for j in range(i + 1, 4):
        original_distances.append(distance(corners[i], corners[j]))

# Calculate distances for the rotated square
rotated_distances = []
for i in range(4):
    for j in range(i + 1, 4):
        rotated_distances.append(distance(rotated_corners[i], rotated_corners[j]))

# Verify that distances are preserved (within a small tolerance)
tolerance = 1e-10
preserved = all(abs(d1 - d2) < tolerance for d1, d2 in zip(original_distances, rotated_distances))
print("Rotation preserves distances:", preserved)
