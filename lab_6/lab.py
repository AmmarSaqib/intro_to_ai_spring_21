"""
Lab 6: KNN

For this lab you be implementing K Nearest Neighbour algorithm on a Dataset.
You'll be using libraries with KNN functions.
We will use two variants of the KNN algorithm in the sklearn library.

In order to install sklearn type the following in your terminal/cmd:
pip install sklearn -> for windows
pip3 install sklearn -> linux based OS

If you get an error that pip is not installed on the system. Kindly 
install pip it can be done separately and also by reinstalling python and 
making sure that you ticked the pip checkbox.

SKlearn has two variants of the algorithm a Classifier and a Regressor.


TASK 1: 
For this task we will use the KNN as a classifier: https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html

The dataset to be used for this will be the "Iris dataset" that you can
load from sklearn. (https://scikit-learn.org/stable/modules/classes.html#module-sklearn.neighbors)

Split the dataset into test and train sets. Use sklearn's test train split function.
Use the default parameters for the classifier and fit a model on this dataset.
Print the accuracy on the test data

"""