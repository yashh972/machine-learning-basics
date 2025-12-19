import pandas as pd
from sklearn.linear_model import LinearRegression

data=pd.read_csv("Code3.csv")
print(data.isnull().sum())
data=data.dropna()

features=data[["area","bedrooms"]]
target=data["price"]



model =LinearRegression()
model.fit(features.values,target)

area=float(input("Please Enter area: "))
bedrooms=int(input("Please Enter bedroom : "))
price=model.predict([[area,bedrooms]])

print("The Price is ",price)