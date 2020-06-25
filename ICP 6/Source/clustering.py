import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
data = pd.read_csv('CC.csv')
# Question 1
# Question 1.a
# Removing the null values and replacing them by the mean value
l = data.isnull().sum()
print(l)
s = data['MINIMUM_PAYMENTS'].isnull().sum()
j = data['CREDIT_LIMIT'].isnull().sum()
c = data['MINIMUM_PAYMENTS'].mean()
d = data['CREDIT_LIMIT'].mean()
data = data.apply(lambda s:s.fillna(c), axis=0)
data = data.apply(lambda j:j.fillna(d), axis=0)
l = data.isnull().sum()
print(l)
# Question 1.b
# Using the elbow method to find a good number of clusters
wcss = []
x = data.iloc[:, 1:17]
y = data.iloc[:, -1]
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, max_iter=100, random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.xlabel('Number of Clusters')
plt.ylabel('wcss')
plt.show()
# Question 2
# From the above plot, at k=3 seem like data slowly un change => choose k=3
# calculating Silhouette score for above clustering
km = KMeans(n_clusters=3, random_state=0)
km.fit(x)
kmeans = km.predict(x)
y_cluster_kmeans = km.predict(x)
score = metrics.silhouette_score(x, y_cluster_kmeans)
print('Silhouette score for', 3, 'clusters', score)
# Question 3
# feature scaling to check whether Silhouette score improved or not
scaler = preprocessing.StandardScaler()
scaler.fit(x)
x_scalar = scaler.transform(x)
x_scaled = pd.DataFrame(x_scalar, columns=x.columns)

km = KMeans(n_clusters=3)
km.fit(x_scaled)
y_cluster_kmeans = km.predict(x_scaled)
feature_scaling_score = metrics.silhouette_score(x_scaled, y_cluster_kmeans)
print('Silhouette score for', 3, 'clusters after scaled', feature_scaling_score)
# Question 4
# Apply PCA on the same data set using two features
pca = PCA(2)
x_pca = pca.fit_transform(x_scaled)

# BONUS QUESTIONS
# Applying k-means algorithm on the PCA result reporting observation if the score has improved or not
# 1.a PCA + K-MEANS
km_1 = KMeans(n_clusters=3, random_state=0)
km_1.fit(x_pca)
y_cluster_kmeans_1 = km_1.predict(x_pca)
pca_score = metrics.silhouette_score(x_pca, y_cluster_kmeans_1)
print("PCA + K-Means Score is :", pca_score)

# Plotting PCA + K-Means
plt.scatter(x_pca[:, 0], x_pca[:, 1], c=y_cluster_kmeans_1)
plt.title('PCA + K-Means')
plt.show()

# 1.b Bonus with PCA + K-Means + scaling (For scaling i uses x_scalar instead of direct data(x))
x_pcascale = pca.fit_transform(x_scalar)
km = KMeans(n_clusters=3)
km.fit(x_pcascale)
Y_cluster_kmeans= km.predict(x_pcascale)
pca_means_scale_score = metrics.silhouette_score(x_pcascale, Y_cluster_kmeans)
print('PCA + K-MEANS + Scale score is:', pca_means_scale_score)

# 2. Plotting the graph for Bonus Q1
plt.scatter(x_pca[:, 0], x_pca[:, 1], c=Y_cluster_kmeans)
plt.title('PCA + K-Means + Scaling')
plt.show()
