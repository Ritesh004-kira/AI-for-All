import numpy as np
import random
A= np.array([[1, 2], [3, 4]])
B= np.array([[5, 6], [7, 8]])
# Addition
print(f"(A + B) = {A + B}")
# Subtraction
print(f"(A - B) = {A - B}")
# Dot Product
print(f"(A . B) = {np.dot(A, B)}")
# Magnitude of A
print(f"|A| = {np.linalg.norm(A)}")
# Cosine
print(f"Cosine of angle between A and B = {np.dot(A.flatten(), B.flatten()) / (np.linalg.norm(A) * np.linalg.norm(B)):.4f}")


# Normalization
A_normalized = A / np.linalg.norm(A)
print(f"Normalized A = {A_normalized}")

#A simple neural network layer using vectors
W = np.random.randn(2,3) * 0.01  # Weights
X = np.array([0.5, 0.2])  # Input
Z = np.dot(X, W)  # Linear transformation
print(f"Output of the layer (Z) = {Z}")

# Rank
print(f"Rank of A = {np.linalg.matrix_rank(A)}")

## Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print(f"Eigenvalues of A = {eigenvalues}")
print(f"Eigenvectors of A = {eigenvectors}")

# Cross Product (for 3D vectors)
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
cross_product = np.cross(v1, v2)
print(f"Cross Product of v1 and v2 = {cross_product}")

# Projection of v1 onto v2
projection = (np.dot(v1, v2) / np.dot(v2, v2)) * v2
print(f"Projection of v1 onto v2 = {projection}")

# QR Decomposition
Q, R = np.linalg.qr(A)
print(f"Q is orthogonal: {np.allclose(Q @ Q.T, np.eye(3))}")
print(f"R is upper triangular: {np.allclose(R, np.triu(R))}")
