# Verify that the Gram-Schmidt output is truly orthonormal: check that every pair has dot product 0 and every vector has magnitude 1
import numpy as np
def gram_schmidt(vectors):
    orthogonal_vectors = []
    for v in vectors:
        w = v.copy()
        for u in orthogonal_vectors:
            proj = np.dot(w, u) / np.dot(u, u) * u
            w = w - proj
        orthogonal_vectors.append(w)
    return orthogonal_vectors
# Example usage
def check_orthonormality():
    vectors = [np.array([1, 1, 0]), np.array([1, 0, 1]), np.array([0, 1, 1])]
    orthogonal_vectors = gram_schmidt(vectors)
    # Check orthogonality and normalization
    for i in range(len(orthogonal_vectors)):
        for j in range(i + 1, len(orthogonal_vectors)):
            dot_product = np.dot(orthogonal_vectors[i], orthogonal_vectors[j])
            print(f"Dot product of vector {i} and vector {j}: {dot_product:.4f}")
        magnitude = np.linalg.norm(orthogonal_vectors[i])
        print(f"Magnitude of vector {i}: {magnitude:.4f}")

check_orthonormality()
