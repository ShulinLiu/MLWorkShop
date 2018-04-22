# scikit-learn examples
from sklearn import datasets
from sklearn import svm

# load dataset
iris = datasets.load_iris()
digits = datasets.load_digits()

print(iris.feature_names)
print(iris.target_names)
print(iris.data[0])
print(iris.target[0])
# for i in range(len(iris.target)):
# 	print("Examples %d Label %s features %s"%(i,iris.target[i],iris.data[i]))

# predict
clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(digits.data[:-1], digits.target[:-1]) 
clf.predict(digits.data[-1:])