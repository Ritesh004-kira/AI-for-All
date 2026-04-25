# Given 5 random word-like vectors (dimension 50), find the two most similar using cosine similarity
import numpy as np
# Generate 5 random word-like vectors of dimension 50
vectors = np.random.rand(5, 50)
# Function to calculate cosine similarity
def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    magnitude_vec1 = np.linalg.norm(vec1)
    magnitude_vec2 = np.linalg.norm(vec2)
    if magnitude_vec1 == 0 or magnitude_vec2 == 0:
        return 0.0
    return dot_product / (magnitude_vec1 * magnitude_vec2)

# Find the two most similar vectors
def find_most_similar(vectors):
    max_similarity = -1
    most_similar_pair = (0, 1)
    for i in range(5):
        for j in range(i + 1, 5):
            similarity = cosine_similarity(vectors[i], vectors[j])
            if similarity > max_similarity:
                max_similarity = similarity
                most_similar_pair = (i, j)

    print(f"Most similar vectors: {most_similar_pair}")
    print(f"Similarity: {max_similarity:.2f}")
    
find_most_similar(vectors)