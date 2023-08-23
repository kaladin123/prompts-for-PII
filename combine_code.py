from sentence_transformers import SentenceTransformer
import numpy as np

# Load the Pretrained Model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Generate Embeddings
def generate_embeddings(features, model):
    return {feature: model.encode([feature])[0] for feature in features}

# Cosine Similarity Function
def cosine_similarity(embedding1, embedding2):
    return np.dot(embedding1, embedding2) / (np.linalg.norm(embedding1) * np.linalg.norm(embedding2))

# Combine Features
def combine_features(grouped_features, categorized_features, model, threshold=0.8):
    grouped_embeddings = generate_embeddings([item for sublist in grouped_features for item in sublist], model)
    
    for category, features in categorized_features.items():
        for feature in features:
            feature_embedding = model.encode([feature])[0]
            for grouped_feature in grouped_features:
                for gf in grouped_feature:
                    if cosine_similarity(feature_embedding, grouped_embeddings[gf]) >= threshold:
                        if gf not in features:
                            features.append(gf)

grouped_features_based_on_embeddings = [
    ['outlook integration'],
    ['call blocking'],
    ['pc connectivity'],
    ['number of handsets'],
    ['landline service requirement'],
    ['hands-free speakerphone'],
    ['camera system'],
    ['cordless phone type'],
    ['display type'],
    ['comfortable grip', 'connectivity'],
    ['conference calling'],
    ['link up to mobile numbers'],
    ['caller id'],
    ['voice assist functionality'],
    ['night mode'],
    ['chipset'],
    ['telephone communication'],
    ['magsafe accessories'],
    ['answering machine storage']
]

features_categorized_based_on_llm = {
    'Integration and Connectivity': ['outlook integration', 'pc connectivity', 'link up to mobile numbers'],
    'Call Features': ['call blocking', 'conference calling', 'caller id'],
    'Handset Features': ['number of handsets', 'cordless phone type', 'comfortable grip'],
    'Phone System Features': ['landline service requirement', 'telephone communication', 'answering machine storage'],
    'Speakerphone and Voice Features': ['hands-free speakerphone', 'voice assist functionality'],
    'Display Features': ['display type', 'night mode'],
    'Camera Features': ['camera system'],
    'Chipset and Accessories': ['chipset', 'magsafe accessories']
}

# Execute the function
combine_features(grouped_features_based_on_embeddings, features_categorized_based_on_llm, model)

print(features_categorized_based_on_llm)
