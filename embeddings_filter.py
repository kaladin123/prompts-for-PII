from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Define the feature names
# feature_names = [
#     # ... [List of feature names you provided]
# ]

# Initialize the sentence transformer model
model = SentenceTransformer('distilbert-base-nli-mean-tokens')

# Get embeddings for each feature name
embeddings = model.encode(feature_names)

# Compute pairwise cosine similarities
cosine_similarities = cosine_similarity(embeddings)

def group_features_by_similarity(threshold):
    grouped_features = []
    visited = set()

    for i in range(len(feature_names)):
        if i not in visited:
            similar_features = [feature_names[i]]
            for j in range(len(feature_names)):
                if i != j and cosine_similarities[i, j] > threshold:
                    similar_features.append(feature_names[j])
                    visited.add(j)
            grouped_features.append(similar_features)
    
    return grouped_features

# Group features with similarity greater than 90%
grouped_features_90 = group_features_by_similarity(0.9)

# Group features with similarity greater than 80%
grouped_features_80 = group_features_by_similarity(0.8)
