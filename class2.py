import csv
import pandas as pd
import plotly.express as px
import math

f=open("class2.csv",newline="")
reader=csv.reader(f)
fileData=list(reader)
fileData.pop(0)

no_of_students=len(fileData)
total=0

for i in fileData:
    total+=float(i[1])

mean=total/no_of_students
print(mean)

df=pd.read_csv("class2.csv")
fig=px.scatter(df,x="Student Number",y="Marks")
fig.update_layout(shapes=[
    dict(type='line',
    y0=mean,y1=mean,
    x0=0,x1=no_of_students
    )
])
fig.show()
squared_list=[]
for number in fileData:
    a=int(number[1])-mean
    a=a**2
    squared_list.append(a)

print(squared_list)
sum=0
for i in squared_list:
    sum=sum+i
result=sum/(len(fileData)-1)
standard_d=math.sqrt(result)

print(standard_d)