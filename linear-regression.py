#######################
#Regression Algorithm##
#######################
import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

#Define data frame as df
df = quandl.get('WIKI/GOOGL')
df = df[['Adj. Open', 'Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100

#Redefine the data frame only for useful data
df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

#Forecast column is defined as Adjusted Stock value at the closed time
forecast_col = 'Adj. Close'

#Non-number will be replaced by -99999
#You cannot give up the whole data because of one missing data column
df.fillna(-99999, inplace=True)

#Round up ten percent of everything to the whole and set it as an integer value
#Take last ten days' data to predict tomorrow
forecast_out = int(math.ceil(0.01 * len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)

x = np.array(df.drop(['label'], 1))
y = np.array(df['label'])
x = preprocessing.scale(X)
y = np.array(df['label'])

x_train, x_test, y_train, y_test = cross.validation.train_test_split(x, y, test_size=0.2)

clf = LinearRegression()
clf.fit(x_train, y_train)
accuracy = clf.score(x_test, y_test)

print (accuracy)
