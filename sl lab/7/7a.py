import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('iris.csv')
df.describe()
df.info()
print(df.head(5))
ax = sns.countplot(data = df,hue = 'Class',palette='Set1',x = ' Sepal_Width')
ax.set(title='Flowers of each specie',xlabel='Sepal Width',ylabel='No. of flowers')
plt.show()
df=df.drop(['Class'],axis=1,inplace=False)
print(df.head(5))
