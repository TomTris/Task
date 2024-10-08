import numpy as np
import pandas as pd

name = "winequality-red.csv"
learning_rate = 0.1
interations = 800

def normalize_score(df):
	citerias = df.columns[0:-1]
	for i in range(len(citerias)):
		old_max = df[citerias[i]].max()
		old_min = df[citerias[i]].min()
		df[citerias[i]] = (df[citerias[i]] - old_min) / (old_max - old_min)
	df['quality'] /= 10.0


def split_rows(df_o, num, qualities):
	df = ([df_o[df_o.values[:, -1] == quality] for quality in qualities])
	
	nrows = int(num * len(df[0]))
	to_train = df[0][:nrows]
	to_test = df[0][nrows:]

	for cnt, df1 in enumerate(df):
		if cnt != 0:
			nrows = int(len(df1) * num)
			df2 = df1[:nrows]
			df3 = df1[nrows:]
			to_train = pd.concat([to_train, df2], ignore_index=True)
			to_test = pd.concat([to_test, df3], ignore_index=True)
	x_train = to_train[to_train.columns[:-1]]
	y_train = to_train[to_train.columns[-1]]
	x_test = to_test[to_test.columns[:-1]]
	y_test = to_test[to_test.columns[-1]]
	return (x_train, y_train, x_test, y_test)


def sigmoid(z):
	return 1 / (1 + np.exp(-z))


def train(x_val, y_val, qualities):
	len_qualities = int(len(qualities))
	qualities_weights = np.zeros([len_qualities, x_val.shape[1] + 1])
	qualities_y_val = np.zeros([x_val.shape[0], len_qualities])
	one_column = np.ones([x_val.shape[0], 1])
	x_val = np.hstack((x_val, one_column))

	for cnt, quality in enumerate(qualities):
		qualities_y_val[:, cnt] = np.where(y_val == np.float64(quality), 1, 0)

	num_samples = x_val.shape[0]

	for _ in range(20000):
		z = np.dot(x_val, qualities_weights.T)
		y_pred = sigmoid(z)
		error = (y_pred - qualities_y_val)
		dw = (1 / num_samples) * np.dot(error.T, x_val)
		qualities_weights -= learning_rate * dw
	return qualities_weights


def	test_model(qualities_weights, x_test, y_test):
	one_column = np.ones([x_test.shape[0], 1])
	x_test = np.hstack((x_test, one_column))
	predictions = sigmoid(np.dot(qualities_weights, x_test.T)) * 100.0
	predictions = np.argmax(predictions, axis=0) + 3
	predictions = np.where(np.float64(predictions) == y_test * 10.0, 1, 0)
	print()
	print("Predicted Result based on logistic Regression:")
	print(f"{sum(predictions) / len(y_test) * 100}%")
	print()


def main():
	df = pd.read_csv(name, sep=';')
	normalize_score(df)
	qualities = np.unique(df.values[:, -1])
	x_train, y_train, x_test, y_test = split_rows(df, 0.8, qualities)
	qualities_weights = train(x_train, y_train, qualities)
	# print weights
	# for weights in qualities_weights:
	# 	for weight in weights:
	# 		print(weight, end=' ')
	# 	print()
	test_model(qualities_weights, x_test, y_test)


if __name__ == "__main__":
	main()