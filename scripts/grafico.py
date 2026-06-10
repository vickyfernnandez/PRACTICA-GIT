import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

datos = pd.read_csv("titanic.csv")

fig,ax =plt.subplots()
sns.countplot(x = "Sex", hue = "Survived", data=datos)
fig.savefig("supervivencia_por_Sexo.png")

fig,ax =plt.subplots()
sns.countplot(x = "Pclass", hue = "Survived", data=datos)
fig.savefig("supervivencia_por_clase.png")
