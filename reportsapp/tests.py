import pandas as pd
from matplotlib import pyplot as plt

from statsmodels.tsa.stattools import adfuller
df=pd.read_csv('MaunaLoaDailyTemps.csv',index_col='DATE')
df=df.dropna()
print('Shape of data',df.shape)
# df.head()
#
# df['AvgTemp'].plot(figsize=(12,5))




def ad_test(dataset):
     dftest = adfuller(dataset, autolag = 'AIC')
     print("1. ADF : ",dftest[0])
     print("2. P-Value : ", dftest[1])
     print("3. Num Of Lags : ", dftest[2])
     print("4. Num Of Observations Used For ADF Regression:",dftest[3])
     print("5. Critical Values :")
     for key, val in dftest[4].items():
         print("\t",key, ": ", val)

ad_test(df['AvgTemp'])

from pmdarima import auto_arima
stepwise_fit = auto_arima(df['AvgTemp'], trace=True,
suppress_warnings=True)

print(df.shape)
train=df.iloc[:-30]
test=df.iloc[-30:]
print(train.shape,test.shape)

from statsmodels.tsa.arima_model import ARIMA

model=ARIMA(train['AvgTemp'],order=(1,0,5))
model=model.fit()
model.summary()
print(model.summary())

start=len(train)
end=len(train)+len(test)-1

pred=model.predict(start=start,end=end,typ='levels').rename('ARIMA Predictions')
pred.plot(legend=True)
test['AvgTemp'].plot(legend=True)
plt.show(test['AvgTemp'])


from sklearn.metrics import mean_squared_error
from math import sqrt
test['AvgTemp'].mean()
rmse=sqrt(mean_squared_error(pred,test['AvgTemp']))
print(rmse)


