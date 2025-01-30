#program to as for name list iput,sort alphabetically and display name count
import re
names=input("Enter a list of names below separated by space:\n").split()
names.sort()
a=names
res =[]
for val in a:
    if val not in res:
        res.append(val)
print(res)
from collections import Counter
input_list =(names)
items = Counter(input_list).keys()
print("Name count is:", len(items))
