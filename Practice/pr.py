# class Car:
    #     def __init__(self,color):
        #         self.__color=color
        #     def start(self):
            #         print(f"{self.color} car started")

            # my_car = Car("Red")
            # print (my_car.__color)
# class Animal:
#     def __init__(self,speak="hello"):
#         self.speak=speak
#     def get_speak(self):
#         print(self.speak)
#     def bark(self):
#         print("lull")
#         animal1=Animal("owwwwwl")
# class Dog(Animal):
#     def bark(self):
#         print("woo")
#         Dog1=Dog()
#         Dog1.bark()
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __str__(self):
#         return f"({self.x},{self.y})"
#     def __add__(self, other):
#         return Point(self.x+other.x,self.y+other.y)  
    
# Point1=Point(2,4)
# Point2=Point(1,9)
# print(Point1)
# print(Point1+Point2)
# import os

# Check where Python thinks it is
# print("Current directory:", os.getcwd())
# print("Files in current directory:", os.listdir())
# with open("duplicate.py","r") as file:
#     data= file.read()
#     print(data)
# filename="student.txt"
# name="Ali"
# Age=18
# try:
#     with open(filename,"r") as file:
#         print(file.read())
# except FileNotFoundError:
#     with open(filename,"w") as file:
#         file.write(f"{name}\n{Age}\n")
#     with open(filename,"r") as file:
#         print(file.read())
# age=-3
# if age<0:
#     raise ValueError("It is negative")
# class invalidageerror(Exception):
#     pass
# age=-3
# if age<0:
#     raise invalidageerror(f"age is negative its error:{age}")
import numpy as np
import time
import pandas as pd
# nparray=np.array([[1,2,3],[2,6,8]])
# print (nparray.shape)
# print(nparray.ndim)
# print(nparray.dtype)
# print (nparray)
# py_list=list(range(1000000))
# start_time=time.time()
# print(start_time)
# result=np.append(nparray,nparray+5,axis=1)
# print (result)
# print(np.ones((2,4)))
# print(np.full((2,4),7.5))
# print(np.arange(0,16,3))
# print(np.linspace(0,5,20))
# print(np.eye(4)) 
# print(np.diag([1,2]))
# arr=np.array([1.5,2.5,6.7])
# print(arr.astype(int))
# arr=np.array([[1,2,5],[8,9,10],[6,5,4]])
# slice_arr=arr[0,:2]
# print(slice_arr)
# copy_arr=arr[:2,:2].copy()
# print(copy_arr)
# arr=np.arange(10000)
# arr=arr**2
# print(arr)
# s=pd.Series(["Ammad","Ali","Daniyal","Ammad","Talha","Aneeq","Shahab"],index=["am","al","da","am","ta","An","Sh"])
# print(s)
# print(s.values, s.dtype)
# print(s.index)
# print(s.dtype)
# print(s.head)
# print(s.tail)
# print(s.value_counts)
# data={
#     'Name':['Alice','Bob','Charlie'],
#     'Age':[25,20,33],
#     'City':['Lahore','Karachi','Islamabad']
# }
# df=pd.DataFrame(data)
# print(df.shape)
# print(df.dtypes)
# print(df.info())
# print(df.describe())
# print(df.loc[0:1,['Name','City']])
# print(df.iloc[0:1,1:2])
# print (df[df['Age']>30])
# df.loc[df['Age']<30,'City']='Hyderabad'
# print(df.loc[df['Age']<30,'City'])
# print(df)
# cleaned_data=my_df[['Sales','Quantity','Date']]
# cleaned_data.to_excel("cleaned.xlsx",sheet_name="Cleaned")
# cleaned_data.to_json("cleaned.json",orient='records',date_format='iso')
# df=pd.read_csv("retail_sales.csv",parse_dates=["Date"],dtype={"Category":"category","Region":"category"})
# df.info()
# my_df=df[df['Sales']>0]
# df['Region']=df["Region"].astype('category')
# print(df)
# print(df.info())
# print(df.memory_usage(deep=True))
# print(df.isna().sum())
# df["Quantity"]=pd.to_numeric(df['Quantity'])
# df["Quantity"]=df["Quantity"].fillna(df["Quantity"].mode()[0])
# print(df.isna().sum())
# df.dropna(subset="Region",inplace=True)
# print(df.isna().sum())
# df_sorted=df.sort_values(by=['Quantity','Sales'],ascending=[False,True])
# print(df_sorted)
# df['Sales_rank'] = df.groupby('Quantity')['Sales'].rank(method='dense', ascending=False)
# print(df)
# customers=pd.DataFrame({
#     "Name":["ali","ahmed","ammad"],
#     "age":[20,25,30],
#     "City":["Lahore","Islamabad","Karachi"]
# })

# df_concat=pd.concat([customers,customers],axis=1)
# print(df_concat)
# def revenuecategory(row):
#     pass
# df["revenue_category"]=df.apply(revenuecategory,axis=1)
# print (df)
from scipy.stats import zscore
df=pd.read_csv("ecommerce_sales_analytics_5000.csv",parse_dates=["order_date"])
df=df.set_index("order_date")
# print(df.index)
# monthlyrevenue=df["revenue"].resample("ME").sum()
# print(monthlyrevenue)
# print(monthlyrevenue.pct_change())
# print(monthlyrevenue.index.is_monotonic_increasing)
# Q1=df["revenue"].quantile(0.25)
# Q3=df["revenue"].quantile(0.75)
# IQR=Q3-Q1
# print(IQR)
# df["revenue_z"]=zscore(df["revenue"])
# outliers_z=df[df["revenue_z"].abs()>3]
# print(outliers_z.shape)
# df=df[df["revenue_z"].abs()<=3]
# print(df.shape)
# numeric_df=df[["revenue","quantity","unit_price","discount","delivery_days"]]
# print(numeric_df.cov())
# print(numeric_df.corr().values.min()*100)
# print(IQR>0)
# nums=[2,5,6,6,7,9,10]
# from collections import Counter
# # counts = Counter(nums)          # done in one line
# # print(counts)
# # print(counts.most_common(1)[0][0])
# # for c1, c2 in zip("flow", "flight"):
# #     print(c1, c2)
# nums = [1, 3, 1, 2, 3, 3,3]
# counts = {}
# for num in nums:
#     counts[num]=counts.get(num,0)+1
# print(counts)
# counts=Counter(nums)
# print(counts.most_common(3)[0][1])
# counts = {"a":3, "b":1, "c":2}
# for key,val in counts.items():
#     print (key, val)
# nums = [1, 2, 3, 4, 5, 6]
# sqr={n:n**3 for n in nums if n%2==0}
# print(sqr)


# print(df.shape)
# print(df.columns)
# print(df.dtypes)
# print(df.head())
# print(df.info())
# print(df.describe())
print(df.isnull().sum())
print(df.duplicated().sum())
import matplotlib.pyplot as plt
df['revenue'].hist(bins=30)
plt.title('Revenue Distribution')
plt.show()
df["customer_rating"].describe()
df['product_category'].value_counts()
df['region'].value_counts()

df['product_category'].value_counts().plot(kind='bar')
plt.title('Product Category Distribution')
plt.show()
df[['revenue', 'unit_price', 'discount', 'quantity', 'delivery_days', 'customer_rating']].corr()
# Histogram for multiple numerical columns at once
df[['revenue', 'unit_price', 'discount', 'delivery_days']].hist(bins=20, figsize=(12, 8))
plt.tight_layout()
plt.show()
import seaborn as sns
import matplotlib.pyplot as plt

# # Step 1 — define which columns are numerical
# numerical_cols = ['revenue', 'unit_price', 'discount', 'quantity', 'delivery_days', 'customer_rating']

# # Step 2 — compute correlation matrix
# corr_matrix = df[numerical_cols].corr()
# print(corr_matrix)

# # Step 3 — visualize it as a heatmap
# plt.figure(figsize=(8, 6))
# sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
# plt.title('Correlation heatmap')
# plt.show()
# df.groupby('product_category')['revenue'].mean()
# df.groupby('region')['revenue'].sum().plot(kind='bar')
# df.groupby('payment_method')['customer_rating'].mean()
df=pd.read_csv("ecommerce_sales_analytics_5000.csv",parse_dates=["order_date"])
print(df.columns)
df['order_date'] = pd.to_datetime(df['order_date'])
df['month'] = df['order_date'].dt.to_period('M')  # fixed here

monthly_revenue = df.groupby('month')['revenue'].sum()
monthly_revenue.plot()
plt.title('Monthly revenue trend')
plt.show()
# df['order_date'] = pd.to_datetime(df['order_date'])
# df['month'] = df['order_date'].dt.to_period('M')  # fixed here

# monthly_revenue = df.groupby('month')['revenue'].sum()
# monthly_revenue.plot()
# plt.title('Monthly revenue trend')
# plt.show()
