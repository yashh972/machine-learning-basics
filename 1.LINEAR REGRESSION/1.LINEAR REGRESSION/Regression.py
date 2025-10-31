import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression


data=pd.read_csv("Code1.csv")
features=data[["area"]]

target=data["price"]

model =LinearRegression()
model.fit(features.values,target)

plt.figure(figsize=(10,5))
plt.scatter(data["area"],data["price"])
plt.plot(data["area"],model.predict(features))
plt.title("Powoi")
plt.xlabel("Area")
plt.ylabel("Price")
plt.show()