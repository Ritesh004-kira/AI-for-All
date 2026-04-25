# Create a 3x3 matrix with rank 2. Verify using the rank() method. Then explain what geometric object the columns span.
import numpy as np
# Create a 3x3 matrix with rank 2
matrix = np.array([[1, 2, 3],
                     [4, 5, 6],
                        [5, 7, 9]])  # This row is a linear combination of the first two rows
# Verify the rank
rank = np.linalg.matrix_rank(matrix)
print(f"Rank of the matrix: {rank}")
# Explanation of the geometric object the columns span
if rank == 2:
    print("The columns of the matrix span a 2-dimensional subspace in 3D space, which can be visualized as a plane.")

