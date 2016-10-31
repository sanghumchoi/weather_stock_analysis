import pandas as pd
from sklearn import cross_validation, neighbors, metrics, linear_model, learning_curve, naive_bayes, svm, ensemble, tree
import os

os.chdir("/home/choiboy9106/Desktop/Metis/Project McNulty")

df = pd.read_csv("testingchi.csv")
