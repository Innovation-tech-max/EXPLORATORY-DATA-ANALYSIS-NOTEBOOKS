# -*- coding: utf-8 -*-
"""EDA:auto_mpg(-Mukut).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1--e8m9oi3tV4-4-ADp97Z-ONOLfx3xCB

# **EXPLORATORY DATA ANALYSIS**

## Importing the necessary libraries.
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import pylab as py
# %matplotlib inline

"""## Reading the dataset."""

df=pd.read_csv("auto-mpg.csv")

"""## A glimpse of our data"""

df.head()

df.tail()

"""## **Basic info & statistics:**

## Size of our data
"""

df.shape

"""There are 398 rows and 9 columns we are going to deal with.

## Features in our data
"""

df.columns

"""The above are the feature names in our data.

## Datatypes' summary
"""

df.info(null_counts=False)

"""The dataframe includes the above datatypes, i.e, float64,int64 and object types."""

df.horsepower = df.horsepower.astype('float')
df.dtypes

"""We get an error as there is "?" present in the horsepower feature values, which is probably a replacement for Nan. We will deal with it in the "Checking for missing values" section.

## Descriptive Statistics
"""

df.describe() #numeric

"""Few important insights from the above are as follows:
*   The mean amount of fuel used by the cars is 23.514573 mpg.
*   The average weight of the cars is 2970.424623 units.
*   The average number of cylinders used in the cars is 5(approx).
*   Minimum amount of fuel used is 9 mpg.
*   Maximum amount of fuel used is 46.6 mpg.







"""

df["car name"].describe()      #categorical

"""*   There are 305 unique car names in our data.
*   ford pinto has the highest frequency count in our data.
*   The number of time "ford pinto" has appeared is 6.

## Checking for missing values
"""

df.isnull().sum()

df.horsepower.unique()

"""To deal with the missing values in horsepower feature:"""

df= df.replace({ "?": np.nan, "&": np.nan })

df.isnull().sum()

"""Since the number of null values is less, they can be dropped directly."""

df=df.dropna(thresh=None, subset=None, inplace=False)

df.isnull().sum().sum()

"""The data is hence clean.

## **Visualisation of the data**
"""

df.plot()

corr = df.corr()
plt.figure(figsize=(8,8))
sns.heatmap(corr,annot=True,cbar=False,cmap='viridis')
plt.show()

"""The above heatmap with its insight of correlation among the features will help for further visualisations and extractions of the facts in the data.
Here,


*   "cylinders" is highly correlated with "displacement".
*   "mpg" is highly correlated with "origin".
*   "displacement" is highly correlated with "weight".
*   "displacement" is highly correlated with "cylinders".
*   "mpg" is highly correlated with "model year".






"""

plot1= df[["model year","weight"]].groupby("model year").aggregate(np.sum)
plot1.plot()

"""From above line graph, we can infer that with year passing by, the cars being manufactured have less weight in comparision to earlier years.

During the years of 72-74, the cars had the maximum weight. During 80s, the cars had the least weight.
"""

plot2= df[["model year","mpg"]].groupby("model year").aggregate(np.sum)
plot2.plot()

"""Another insight is that mpg with respect to model year has been increasing.

### Checking for the distribution of mpg:
"""

sns.distplot(df['mpg'])

a = np.random.normal(0, 1, 100)    
sm.qqplot(df['mpg'], line ='45')
py.show()

"""The above is the Q-Q plot explaining that the distribution of 'mpg' is skewed, i.e, not exactly normal."""