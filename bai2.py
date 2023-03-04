import pandas as pd
data = pd.read_excel('input.xlsx', skiprows=10, nrows=52,usecols=range(9))
# data.head()
# print(data)
list= [data]
list.sort(reverse=True)
# print(list)
print(list)
