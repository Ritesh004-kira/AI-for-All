# Implement Vector.angle_between(other) that returns the angle in degrees between two vectors
import numpy as np
class Vector:
    def __init__(self, components):
        self.components = np.array(components)

    def angle_between(self, other):
        dot_product = np.dot(self.components, other.components)
        magnitude_self = np.linalg.norm(self.components)
        magnitude_other = np.linalg.norm(other.components)
        cosine_angle = dot_product / (magnitude_self * magnitude_other)
        angle_radians = np.arccos(cosine_angle)
        angle_degrees = np.degrees(angle_radians)
        return angle_degrees    
# Example usage
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
angle = v1.angle_between(v2)
print(f"Angle between v1 and v2: {angle:.2f} degrees")
