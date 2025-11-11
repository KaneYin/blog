K-means Clustering is an unsupervised machine learning algorithm that helps group data points into clusters based on their inherent similarity. Unlike supervised learning, where we train models using labeled data, K-Means is used when we have data that is not labeled and the goal is to uncover hidden patterns or structures. For example, an online store can use K-Means to segment customers into groups like "Budget Shoppers", "Frequent Buyers" and "Big Spenders" based on their purchase history.

# Working of K-Means Clustering

The algorithm will categorize the items into "k" groups of clusters of similarity. To calculate that similarity we will use the **Educlidean distance** as a measurement. The algorithm works as follows:
1. Initialization: We begin by randomly selecting k cluster centroids.
2. Assignment Step: Each data point is assigned to the nearest centroid, forming clusters.
3. Update Step: After the assignment, we recalculate the centroid of each cluster by averaging the points within it.
4. Repeat: This process repeats until the centroids no longer change or the maximum number of iterations is reached.

# Why use K-Means Clustering?
K-Means is popular in a wide variety of applications due to its simplicity, efficiency and effectiveness. Here's why it is widely used:
1. Data Segmentation: 
2. Image Compression: 
3. Anomaly Detection: 
4. Document Clustering: 
5. Organizing Large Database: 


# Implementation of K-Means Clustering
We will be using blobs datasets and show how clusters are made using python programming language.

## Step 1: Importing the necessary libraries
We will be importing the following libraries.
- Numpy: for numerical operations.
- Matplotlib: for plotting data and results.
- Scikit learn: to create a synthetic dataset using **make_blobs** .

## Step 2: Creating custom dataset

we will generate a synthetic dataset with make_blobs.

- `make_blobs(n_samples=500, n_features=2, centers=3)`: Generate 500 data points in a 2-D space, grouped into 3 clusters.
- `plt.scatter[x]`
- `plt.show()`: display the plot


# Reference
