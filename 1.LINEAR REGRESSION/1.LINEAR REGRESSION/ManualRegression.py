import pandas as pd
from sklearn.linear_model import LinearRegression

data=pd.read_csv("Code1.csv")
features=data[["area"]]
target=data["price"]
model =LinearRegression()
model.fit(features.values,target)

area=float(input("Please Enter Area: "))
price=model.predict([[area]])

m=model.coef_
c=model.intercept_

print("M is",m)
print("C is",c)

print("The Price is ",price)