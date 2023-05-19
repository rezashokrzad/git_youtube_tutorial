MNIST Handwritten Digit Classification: Build a machine learning model that can correctly classify handwritten digits from the MNIST dataset.
## MNIST handwritten digits classification with KNN (Mohammadreza Tale Akmal)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

X, y = fetch_openml('mnist_784', version=1, return_X_y=True, as_frame=False)

print('x_shape =', X.shape)
print('y_shape =',y.shape)

set(y)

sample = 22
print('Label= ', y[sample])
image = X[sample].reshape(28,28)
plt.imshow(image, cmap='gray')
plt.show()

# change background color
X = 255 - X

sample = 22
print('Label= ',y[sample])
image = X[sample].reshape(28,28)
plt.imshow(image, cmap='gray')
plt.show()

# split data to train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# scaling data
from sklearn.preprocessing import MinMaxScaler
m = MinMaxScaler()
X_train = m.fit_transform(X_train)
X_test = m.transform(X_test)

# choose best k_neighbors ... It takes approximately 8 minutes.
from sklearn.model_selection import GridSearchCV

# Define the parameter grid
param_grid = {'n_neighbors': [3, 5, 7]}

# Create a KNN classifier
knn = KNeighborsClassifier()

# Create a GridSearchCV object
grid_search = GridSearchCV(knn, param_grid, cv=5)

# Fit the training data to perform the grid search
grid_search.fit(X_train, y_train)

# Print the best parameters and the corresponding score
print("Best parameters: ", grid_search.best_params_)
print("Best score: ", grid_search.best_score_)

# Evaluate the model on the test data
accuracy = grid_search.score(X_test, y_test)
print("Test accuracy: ", accuracy)

# Training model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Evaluating model performance
print('accuracy = ',knn.score(X_test,y_test))
