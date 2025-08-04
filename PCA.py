import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Sample numeric DataFrame
df = pd.DataFrame({
    'A': [10, 20, 30, 40],
    'B': [5, 15, 25, 35],
    'C': [100, 80, 60, 40]
})

# Step 1: Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# Step 2: Apply PCA
pca = PCA(n_components=2)  # You can choose n_components based on your needs
X_pca = pca.fit_transform(X_scaled)

# Step 3: Put results into a DataFrame
df_pca = pd.DataFrame(X_pca, columns=['PC1', 'PC2'])
print("PCA Result:\n", df_pca)

# Step 4: Explained variance
print("\nExplained Variance Ratio:", pca.explained_variance_ratio_)
print("Cumulative Explained Variance:", pca.explained_variance_ratio_.cumsum())

# Step 5: Scree plot
pca_full = PCA()
pca_full.fit(X_scaled)

plt.figure(figsize=(6,4))
plt.plot(range(1, len(pca_full.explained_variance_ratio_)+1),
         pca_full.explained_variance_ratio_.cumsum(),
         marker='o', linestyle='--')
plt.xlabel('Number of Principal Components')
plt.ylabel('Cumulative Explained Variance')
plt.title('Scree Plot (Elbow Curve)')
plt.grid(True)
plt.show()
