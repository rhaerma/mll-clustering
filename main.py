from sklearn import datasets
from sklearn.model_selection import train_test_split

import sklearn.cluster as sklearn_cluster
import knn
import metrics

iris = datasets.load_iris()
X = iris.data
y = iris.target
n_clusters = len(iris.target_names)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
print("Total train dataset: ", len(y_train))
print("Total test dataset: ", len(y_test))

print("\n===========================\n")

print("KNN Clustering from Scratch")
kmeans = knn.KMeans(n_clusters).fit(X_train)
y_predict = kmeans.predict(X_test)

confusion_matrix = metrics.cluster_confusion_matrix(n_clusters, y_predict, y_test)
print("Confusion Matrix:")
print(confusion_matrix)

print("Accuracy:")
accuracy_score = metrics.cluster_accuracy_score(y_predict, y_test, confusion_matrix)
print(">", accuracy_score)

print()

print("KNN Clustering SKLearn")
skl_kmeans = sklearn_cluster.KMeans(n_clusters).fit(X_train)
y_predict = skl_kmeans.predict(X_test)

confusion_matrix = metrics.cluster_confusion_matrix(n_clusters, y_predict, y_test)
print("Confusion Matrix:")
print(confusion_matrix)

print("Accuracy:")
accuracy_score = metrics.cluster_accuracy_score(y_predict, y_test, confusion_matrix)
print(">", accuracy_score)

print("\n===========================\n")

