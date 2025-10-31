import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv("Code1.csv")
X=data["area"]
Y=data["price"]
plt.figure(figsize=(10,5))
plt.scatter(X,Y,color="red")
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Powoi Estate Rate")
plt.show()
