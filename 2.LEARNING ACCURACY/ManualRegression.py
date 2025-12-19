import pandas as pd
from sklearn.linear_model import LinearRegression

data=pd.read_csv("Code2 - Copy.csv")
print(data.isnull().sum())
data=data.dropna()

features=data[["years"]]
target=data["salary"]



model =LinearRegression()
model.fit(features.values,target)

m=model.coef_
c=model.intercept_

years=int(input("Please Enter Year: "))
salary=m * years + c

print("The Salary is ",salary)