import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import cross_validation, neighbors, metrics, linear_model, learning_curve, naive_bayes, svm, ensemble, tree
import os

os.chdir("/home/choiboy9106/Desktop/Metis/Project McNulty")

# Reading in CSV File into Pandas DataFrame
df = pd.read_csv("all2.csv")
testingdf = pd.read_csv("testingchi.csv")

# Creating X and Y variables + cross validation sets
x = df.iloc[:,:-1]
y = df.iloc[:,-1:]
# print(df.columns)
# print(x)
# print(y)
x_train, x_test, y_train, y_test = cross_validation.train_test_split(x, y, test_size = 0.3, random_state = 4444)

# Data Visualization
countupdown = y["Direction"].value_counts()
upcount = countupdown["Up"]
downcount = countupdown["Down"]
print(upcount)
print(downcount)

objects = ["Up", "Down"]
count = [upcount, downcount]
y_pos = np.arange(len(objects))
plt.xticks(y_pos, objects)
plt.ylabel("Count of Up and Downs")
plt.xlabel("Directional Movement")
plt.title("Count of Upward and Downward Movement of Stock Market")
plt.show(plt.bar(y_pos, count, align = "center", alpha = 0.5))

# Classifier Functions
# K Nearest Neighbors
neigh = neighbors.KNeighborsClassifier(n_neighbors = 9)
neigh.fit(x_train, y_train)
predict = neigh.predict(x_test)
print("K Nearest Classifier")
# print(predict)
print(metrics.accuracy_score(y_test, predict))
# print(neigh.predict_proba(testingdf))
knnclassifier = pd.DataFrame(neigh.predict_proba(testingdf))

# Logistic Regression
log_regression = linear_model.LogisticRegression()
log_regression.fit(x_train, y_train)
predict_log = log_regression.predict(x_test)
print("Logistic Regression")
# print(predict_log)
print(metrics.accuracy_score(y_test, predict_log))
# print(log_regression.predict_proba(testingdf))
logclassifier = pd.DataFrame(log_regression.predict_proba(testingdf))

# Decision Tree Classifer
treereg = tree.DecisionTreeClassifier()
treereg.fit(x_train, y_train)
predicttree = treereg.predict(x_test)
print("Decision Tree")
# print(predicttree)
print(metrics.accuracy_score(y_test, predicttree))
# print(treereg.predict_proba(testingdf))
treeclassifier = pd.DataFrame(treereg.predict_proba(testingdf))

# Extra Tree Classifier
extrareg = tree.ExtraTreeClassifier()
extrareg.fit(x_train, y_train)
predictextree = extrareg.predict(x_test)
print("Extra Tree Classifier")
# print(predictextree)
print(metrics.accuracy_score(y_test, predictextree))
# print(extrareg.predict_proba(testingdf))
extraclassifier = pd.DataFrame(extrareg.predict_proba(testingdf))

# Random Forest Classifier
forestreg = ensemble.RandomForestClassifier()
forestreg.fit(x_train, y_train)
predictforest = forestreg.predict(x_test)
print("Random Forest Classifier")
# print(predictforest)
print(metrics.accuracy_score(y_test, predictforest))
# print(forestreg.predict_proba(testingdf))
forestclassifier = pd.DataFrame(forestreg.predict_proba(testingdf))

# Ada Boosted Classifier
adareg = ensemble.AdaBoostClassifier()
adareg.fit(x_train, y_train)
predictada = adareg.predict(x_test)
print("Ada Boosting Classifier")
# print(predictada)
print(metrics.accuracy_score(y_test, predictada))
# print(adareg.predict_proba(testingdf))
adaclassifier = pd.DataFrame(adareg.predict_proba(testingdf))

# Gradient Boosting Classifier
boostreg = ensemble.GradientBoostingClassifier()
boostreg.fit(x_train, y_train)
predictboost = boostreg.predict(x_test)
print("Gradient Boosting Classifier")
# print(predictboost)
print(metrics.accuracy_score(y_test, predictboost))
# print(boostreg.predict_proba(testingdf))
boostingclassifier = pd.DataFrame(boostreg.predict_proba(testingdf))

classifier = pd.concat([knnclassifier, logclassifier, treeclassifier, extraclassifier, forestclassifier, adaclassifier, boostingclassifier], axis = 1)
classifier.columns = ["KNN", "KNN-1", "Logistic", "Logistic-1", "Trees", "Trees-1", "Extra Trees", "Extra Trees-1", "Forest", "Forest-1", "Ada", "Ada-1", "Boosting", "Boosting-1"]
del classifier["KNN-1"]
del classifier["Logistic-1"]
del classifier["Trees-1"]
del classifier["Extra Trees-1"]
del classifier["Forest-1"]
del classifier["Ada-1"]
del classifier["Boosting-1"]
# print(classifier.head())
classifier.to_csv("classifer_chi.csv")
