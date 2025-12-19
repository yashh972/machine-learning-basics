import pandas as pd
from sklearn.linear_model import LinearRegression

data=pd.read_csv("Code2 - Copy.csv")
print(data.isnull().sum())
data=data.dropna()

features=data[["years"]]
target=data["salary"]



model =LinearRegression()
model.fit(features.values,target)

years=int(input("Please Enter Year: "))
salary=model.predict([[years]])

print("The Salary is ",salary)