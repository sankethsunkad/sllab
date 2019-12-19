import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("train.csv")
print(df)
df.describe()
df.info()
df=df.drop(['Fare'],axis=1, inplace=False)
print(df.head(5))
df['Survived']=df['Survived'].fillna('Not known')
print(df.head(5))
df ['Survived'] = df ['Survived'].map({0: 'Died', 1: 'Survived'})
ax = sns.countplot(x = 'Pclass', hue = 'Survived', palette = 'Set1',data = df)
ax.set(title = 'Passenger status (Survived/Died) against Passenger Class',xlabel = 'Passenger Class', ylabel = 'Total')
plt.show()