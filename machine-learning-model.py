import numpy as np
import pandas as pd
from random import randrange
from math import exp

#load the dataset from csv file
def load_data(filename):
	data = pd.read_csv(filename, names = ['Price', 'Ratings', 'No of Ratings', 'RAM', 'ROM', 'Display(cm)', 'cameraQ(MP)', 'Label'])
	data = np.array(data)
	data = data[1:]
	remove_indx = []
	for i in range(data.shape[0]):
		if data[i][7] == '-1':
			remove_indx.append(i)
			
	data = np.delete(data, remove_indx, axis = 0)
	return data

#convert string to float in dataset
def str_to_float(data):
	for i in range(data.shape[0]):
		for j in range(data.shape[1]):
			data[i][j] = float(data[i][j])
	return data

#get appropriate value of y from probabilities in dataset
def y_from_prob(data):
	for i in range(data.shape[0]):
		if data[i][7] >= 0.6:
			data[i][7] = 1.0
		else:
			data[i][7] = 0.0
	return data

#find minmax for each column to use to rescale later
def data_minmax(data):
	minmax = []
	for i in range(len(data[0])):
		col = [row[i] for row in data]
		min_val = min(col)
		max_val = max(col)
		minmax.append([min_val, max_val])
	return minmax

#rescale dataset to be between 0 and 1
def normalize(data, minmax):
	for row in data:
		for i in range(len(row)):
			row[i] = (row[i] - minmax[i][0])/(minmax[i][1] - minmax[i][0])

#for evaluation of algorithm
def cross_validation_split(data, n_folds):
	data_split = []
	data_copy = list(data)
	fold_size = int(len(data)/ n_folds)
	for i in range(n_folds):
		fold = []
		while len(fold) < fold_size:
			index = randrange(len(data_copy))
			fold.append(data_copy.pop(index))
		data_split.append(fold)
	return data_split

#find accuracy %
def accuracy(real, predicted):
	correct = 0
	for i in range(len(real)):
		if(real[i] == predicted[i]):
			correct += 1
	return (correct/float(len(real))*100.0)

#evaluate the algorithm using cross_validation
def evaluate_algo(data, algo, n_folds, *args):
	folds = cross_validation_split(data, n_folds)
	scores = []
	for fold in folds:
		trainset = list(folds)
		try:
			trainset.remove(fold)
		except ValueError:
			pass
		trainset = sum(trainset, [])
		testset = []
		for row in fold:
			row_copy = list(row)
			testset.append(row_copy)
			row_copy[-1] = None
		predicted = algo(trainset, testset, *args)
		real = [row[-1] for row in fold]
		acc = accuracy(real, predicted)
		scores.append(acc)
	return scores

#make predictions using data and coeffs
def predict(row, coeff):
	yhat = coeff[0]
	for i in range(len(row) - 1):
		yhat += coeff[i+1] * row[i]
	return 1.0/(1+exp(-yhat))

#calculate coeff values for a training dataset using sgd
def coeffs_sgd(train, lr, epochs):
	coef = [0.0 for i in range(len(train[0]))]
	for epoch in range(epochs):
		sum_error = 0
		for row in train:
			yhat = predict(row, coef)
			error = row[-1] - yhat
			sum_error += error**2
			coef[0] = coef[0] + lr*error*yhat*(1.0 - yhat)
			for i in range(len(row) - 1):
				coef[i+1] = coef[i+1] + lr*error*yhat*(1.0 - yhat)*row[i]
		print("-->epoch={}, lr={}, error={}".format(epoch, lr, sum_error))
	return coef

#logistic regression
def logistic_regression(train, test, lr, epochs):
	predictions = []
	coef = coeffs_sgd(train, lr, epochs)
	for row in test:
		yhat = predict(row, coef)
		yhat = round(yhat)
		predictions.append(yhat)
	return predictions



filename = '/home/kmd/projects/api/prod_phone.csv'
data = load_data(filename)
data = str_to_float(data)
data = y_from_prob(data)
minmax = data_minmax(data)
normalized_data = normalize(data, minmax)
n_folds = 2
lr = 0.01
epochs = 20000
scores = evaluate_algo(data, logistic_regression, n_folds, lr, epochs)
print("Scores:{}".format(scores))
print("Mean accuracy:{}".format(sum(scores)/float(len(scores))))


