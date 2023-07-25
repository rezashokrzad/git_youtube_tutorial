#Iris Flower Classification: Build a machine learning model that can correctly classify different species of iris flowers based on their sepal length, sepal width, petal length, and petal width.

import sklearn.datasets as datasets
import pandas as pd

iris=datasets.load_iris()
print(iris)

data=pd.DataFrame(iris.data,columns=iris.feature_names)
data["target"]=iris.target

data.head()
data.tail()

print(iris.target_names)
#Target=0 is "setosa"
#Target=1 is "versicolor"
#Target=2 is "virginica"

data.shape
data["target"].value_counts()
data.describe()
data.info()

import seaborn as sns
import matplotlib.pyplot as plt
sns.pairplot(data,hue="target")

sns.heatmap(data.corr(),annot=True)
plt.show()

X=data.drop("target",axis=1)
y=data["target"]
print(X.shape)
print(y.shape)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=369)

#SVC:

from sklearn.svm import SVC
svc_model=SVC()
svc_model.fit(X_train,y_train)
y_pred=svc_model.predict(X_test)

from sklearn.metrics import classification_report ,confusion_matrix
print(classification_report(y_test,y_pred))
confusion_matrix(y_test,y_pred)

#RandomForest:
from sklearn.ensemble import RandomForestClassifier
RF_model=RandomForestClassifier()
RF_model.fit(X_train,y_train)

p=RF_model.predict(X_test)
print(classification_report(y_test,p))
confusion_matrix(y_test,p)

