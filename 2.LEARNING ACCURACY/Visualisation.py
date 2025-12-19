import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv("Code2 - Copy.csv")
X=data["years"]
Y=data["salary"]
plt.figure(figsize=(10,5))
plt.scatter(X,Y,color="red")
plt.xlabel("Years")
plt.ylabel("Salary")
plt.title("Google SDE")
plt.show()
