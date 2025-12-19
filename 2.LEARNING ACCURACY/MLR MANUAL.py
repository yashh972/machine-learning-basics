import pandas as pd
from sklearn.linear_model import LinearRegression

data=pd.read_csv("Code3.csv")

data=data.dropna()

features=data[["area","bedrooms"]]
target=data["price"]



model =LinearRegression()
model.fit(features.values,target)

m1 = model.coef_[0]
m2=model.coef_[1]
c = model.intercept_
area=float(input("Please Enter area: "))
bedrooms=int(input("Please Enter bedroom: "))
price = m1 * area + m2 * bedrooms + c

print("The Price is ",price)