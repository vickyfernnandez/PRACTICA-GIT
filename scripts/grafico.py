import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

datos = pd.read_csv("titanic.csv")

fig,ax =plt.subplots()
sns.countplot(x = "Sex", hue = "Survived", data=datos)
fig.savefig("plot.png")

fig,ax =plt.subplots()
sns.countplot(x = "Sex", hue = "Pclass", data=datos)
fig.savefig("plot2.png")
