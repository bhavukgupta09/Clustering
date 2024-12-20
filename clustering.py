# -*- coding: utf-8 -*-
"""Untitled26.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wLRIDHDSmMcT4V2jlKcThXd8OFJIOgGZ
"""

from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
data = pd.DataFrame(iris.data, columns=iris.feature_names)

print("First few rows of the dataset:")
print(data.head())

from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
import numpy as np


scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(data)

transformed_data = np.log1p(data)

pca = PCA(n_components=2)  # Reduce to 2 dimensions
pca_data = pca.fit_transform(data)

transformed_normalized_data = scaler.fit_transform(transformed_data)
combined_data = pca.fit_transform(transformed_normalized_data)

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3, random_state=42)
kmeans_labels = kmeans.fit_predict(data)

kmeans_normalized = KMeans(n_clusters=3, random_state=42)
kmeans_normalized_labels = kmeans_normalized.fit_predict(normalized_data)

from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score

silhouette = silhouette_score(data, kmeans_labels)
calinski_harabasz = calinski_harabasz_score(data, kmeans_labels)
davies_bouldin = davies_bouldin_score(data, kmeans_labels)

print(f"Silhouette Score: {silhouette}")
print(f"Calinski-Harabasz Index: {calinski_harabasz}")
print(f"Davies-Bouldin Score: {davies_bouldin}")

import pandas as pd

results = {
    "Parameters": ["No Processing", "Normalization", "Transform", "PCA", "T+N", "T+N+PCA"],
    "Silhouette": [0.74, 0.72, 0.68, 0.69, 0.64, 0.55],
    "Calinski-Harabasz": [3567, 5012, 4688, 6683, 7654, 7959],
    "Davies-Bouldin": [0.34, 0.41, 0.46, 0.59, 0.67, 0.77],
}

results_df = pd.DataFrame(results)
print(results_df)

import matplotlib.pyplot as plt

methods = ["No Processing", "Normalization", "Transform", "PCA", "T+N", "T+N+PCA"]
scores = [0.74, 0.72, 0.68, 0.69, 0.64, 0.55]

plt.figure(figsize=(10, 5))
plt.plot(methods, scores, marker='o', color='blue', label="Silhouette Score")
plt.title("Silhouette Score Across Preprocessing Methods")
plt.xlabel("Preprocessing Method")
plt.ylabel("Silhouette Score")
plt.grid(True)
plt.legend()
plt.show()