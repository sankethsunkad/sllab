import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("blackfri.csv")
df.describe()
df.info()
print(df.head(10))
df['City_Category']=df['City_Category'].fillna('defaultv')
print(df.head(5))
df['City_Category']=df['City_Category'].map({
    'A':'Metro cities','B':'Small Towns','C':'Villages'
})
print(df.head(5))
ax = sns.countplot(data=df,x='Gender',hue='City_Category',palette='Set1')
ax.set(title='Male and Female belonging to each city',xlabel='Gender',ylabel='Count')
plt.show()
