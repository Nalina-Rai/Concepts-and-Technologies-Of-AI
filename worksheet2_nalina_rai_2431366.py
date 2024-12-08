# -*- coding: utf-8 -*-
"""Worksheet2_Nalina_Rai_2431366.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Sg9VAsptcIeKGl6oqdSY6XlAa-3kLKpY
"""

#3.1
#Q.1
import pandas as pd
reader = pd.read_csv("/content/drive/MyDrive/Workshop2/bank .csv")
data_frame = pd.DataFrame(reader)
print(data_frame)

#Q.2
import pandas as pd
reader = pd.read_csv("/content/drive/MyDrive/Workshop2/bank .csv")
data_frame = pd.DataFrame(reader)
# Part (a)
data_type = data_frame.select_dtypes("object").columns
print (data_type)
# Part(b)
for column in data_frame.columns:
    print(f"Unique values in '{column}': {data_frame[column].unique()}")
# part (c)
print("numm values: ",data_frame.isnull())
print("OUTPUT")

#Q.3
import pandas as pd
reader = pd.read_csv("/content/drive/MyDrive/Workshop2/bank .csv")
data_frame = pd.DataFrame(reader)
data_frame =data_frame.select_dtypes(exclude=['object'])
data_frame.to_csv('banknumericdata.csv',index=False)

#Q.4
import pandas as pd
reader = pd.read_csv("/content/drive/MyDrive/Workshop2/bank .csv")
data_frame = pd.DataFrame(reader)
summary = data_frame.describe()
print(summary)

#Problem2
#Q.1
import pandas as pd
reader= pd.read_csv("/content/drive/MyDrive/Workshop2/medical_students_dataset (3).csv")
data_frame = pd.DataFrame(reader)
print(data_frame)

#Q.2
import pandas as pd
reader= pd.read_csv("/content/drive/MyDrive/Workshop2/medical_students_dataset (3).csv")
data_frame = pd.DataFrame(reader)
# print(data_frame)
print("Info of the dataframe: ")
print(data_frame.info())
print("Null values:")
print(data_frame.isnull())

#Q.3
import pandas as pd
from sklearn.datasets import load_iris
import numpy as np
reader= pd.read_csv("/content/drive/MyDrive/Workshop2/medical_students_dataset (3).csv")
data_frame = pd.DataFrame(reader)
missing = data_frame.isnull().sum()
print(missing)
# iris_df_ffill = iris_df.ffill()
# iris_df_mean = iris_df.fillna(iris_df.mean())

#Q.4
import pandas as pd
reader= pd.read_csv("/content/drive/MyDrive/Workshop2/medical_students_dataset (3).csv")
data_frame = pd.DataFrame(reader)
duplicated =data_frame.duplicated()
print(duplicated)
data_frame.drop_duplicates()

#3.2
#Problem1
import pandas as pd
reader = pd.read_csv("/content/drive/MyDrive/Workshop2/Titanic-Dataset.csv")
data_frame = pd.DataFrame(reader)
subset_df = data_frame[['Name', 'Pclass', 'Sex', 'Age', 'Fare', 'Survived']]
selected_datas = subset_df[subset_df['Pclass']==1]
print("3.2 Problem1")
print(selected_datas)

fare_mean = selected_datas['Fare'].mean()
fare_median = selected_datas['Fare'].median()
fare_max = selected_datas['Fare'].max()
fare_min = selected_datas['Fare'].min()

print(f"Mean Fare: {fare_mean}")
print(f"Median Fare: {fare_median}")
print(f"Maximum Fare: {fare_max}")
print(f"Minimum Fare: {fare_min}")

#Problem 2
import pandas as pd
reader = pd.read_csv("/content/drive/MyDrive/Workshop2/Titanic-Dataset.csv")
data_frame = pd.DataFrame(reader)
subset_df = data_frame[['Name', 'Pclass', 'Sex', 'Age', 'Fare', 'Survived']]
selected_datas = subset_df[subset_df['Pclass']==1]
null_valcount =selected_datas['Age'].isnull().sum()
print("The null value count of the age is: ")
print(null_valcount)
data_frame.drop_duplicates(subset=['Age'])

#Problem 3
import pandas as pd
reader = pd.read_csv("/content/drive/MyDrive/Workshop2/Titanic-Dataset.csv")
data_frame = pd.DataFrame(reader)
subset_df = data_frame[['Name', 'Pclass', 'Sex', 'Age', 'Fare', 'Survived']]
selected_datas = subset_df[subset_df['Pclass']==1]
embarked = pd.get_dummies(data_frame['Embarked'],prefix='Embarked')
data_frame = pd.concat([data_frame,embarked],axis = 1)
data_frame = data_frame.drop(columns=['Embarked'])
print(data_frame.head())

#Problem 4
import pandas as pd
reader = pd.read_csv("/content/drive/MyDrive/Workshop2/Titanic-Dataset.csv")
data_frame = pd.DataFrame(reader)
subset_df = data_frame[['Name', 'Pclass', 'Sex', 'Age', 'Fare', 'Survived']]
selected_datas = subset_df[subset_df['Pclass']==1]
survival_rates = data_frame.groupby('Sex')['Survived'].mean()
print(survival_rates)

import matplotlib.pyplot as plt
survival_rates.plot(kind='bar', color=['red', 'black'], alpha=0.7)
plt.title('Mean Survival Rates by Gender')
plt.ylabel('Mean Survival Rate')
plt.xlabel('Gender')
plt.ylim(0, 1)
plt.show()

# Problem 5
import pandas as pd
reader = pd.read_csv("/content/drive/MyDrive/Workshop2/Titanic-Dataset.csv")
data_frame = pd.DataFrame(reader)
subset_df = data_frame[['Name', 'Pclass', 'Sex', 'Age', 'Fare', 'Survived']]
selected_datas = subset_df[subset_df['Pclass']==1]
survival_rates = data_frame.groupby(['Embarked', 'Sex'])['Survived'].mean().unstack()
print(survival_rates)

import matplotlib.pyplot as plt

# Plot grouped bar chart
survival_rates.plot(kind='bar', figsize=(8, 6), color=['yellow', 'green'], alpha=0.7)

# Customize the plot
plt.title('Survival Rates by Port of Embarkation and Gender')
plt.ylabel('Mean Survival Rate')
plt.xlabel('Port of Embarkation')
plt.ylim(0, 1)
plt.legend(title='Gender', labels=['Male', 'Female'])
plt.show()