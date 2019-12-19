import pandas as pd
from pandas import DataFrame,Series
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('StudentsPerformance.csv')
print(df.head(5))
df.info()
df.describe()
df = df.drop(['lunch'], axis=1,inplace = False)
print('\\n====Understanding Inplace False : The Copied Dataframe====')
print(df.head(3))
df['parental level of education'] = df['parental level of education'].fillna('Not Applicable')
print(df)
ax = sns.countplot(x="test preparation course",hue='gender',palette='Set3',data=df)
ax.set(title="Course completion based on gender", xlabel='Course', ylabel='Total')
plt.show()