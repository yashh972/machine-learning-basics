import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


data = pd.read_csv("Code2 - Copy.csv")
data=data.dropna()

features = data[["years"]]
target = data["salary"]

x_train,x_test,y_train,y_test = train_test_split(features.values,target)  #cant change order
print(x_test)
print(y_test)

model = LinearRegression()
model.fit(x_train,y_train)

training_score = model.score(x_train,y_train)
test_score = model.score(x_test,y_test)


print("Training score is ",training_score*100)
print("Testing Score is ",test_score*100)