# -*- coding: utf-8 -*-
"""

@author: pawel
"""

<<<<<<< HEAD
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

<<<<<<< HEAD
=======
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import linear_model

def plot_decision_boundary(pred_func):
    # Set min and max values and give it some padding
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    h = 0.01
    # Generate a grid of points with distance h between them
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    # Predict the function value for the whole gid
    Z = pred_func(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    # Plot the contour and training examples
    plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Spectral)

>>>>>>> 47450aa3f9df38a4b5a12a52b35752297f3c8816

np.random.seed(0)
X, y = datasets.make_moons(100, noise=0.10)
plt.scatter(X[:,0], X[:,1], s=40, c=y, cmap=plt.cm.Spectral)
<<<<<<< HEAD
=======

>>>>>>> f5c9079325fe9ca76032896d6c3b8ef695242ee3
=======

clf=linear_model.LogisticRegressionCV()
clf.fit(X, y)
plot_decision_boundary(lambda x: clf.predict(x))
#plt.title("Logistic Regression")

if __name__ == "__main__":
    pass
>>>>>>> 47450aa3f9df38a4b5a12a52b35752297f3c8816
