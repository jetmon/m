from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

iris = datasets.load_iris()
X = pd.DataFrame(iris.data)
X.columns = ["Sepal_Length","Sepal_Width","Petal_Length","Petal_Width"]

Y = pd.DataFrame(iris.target)
Y.columns = ['Targets']

ColorMap = np.array(['red','blue','green'])

plt.figure(figsize=(14,7))

plt.subplot(1,2,1)
plt.scatter(X.Sepal_Length, X.Sepal_Width,c = ColorMap[Y.Targets],s = 40)
plt.title("Sepal")

plt.subplot(1,2,2)
plt.scatter(X.Petal_Length, X.Petal_Width,c = ColorMap[Y.Targets],s = 40)
plt.title("Petal")
plt.show()

KM_model = KMeans(n_clusters=3)
KM_model.fit(X)

plt.subplot(1,2,1)
plt.scatter(X.Petal_Length, X.Petal_Width,c = ColorMap[KM_model.labels_],s = 40)
plt.title("KMeans")

GM_model = GaussianMixture(n_components=3)
GM_model.fit(X)

plt.subplot(1,2,2)
plt.scatter(X.Petal_Length, X.Petal_Width,c = ColorMap[GM_model.predict(X)],s = 40)
plt.title("GM")
plt.show()