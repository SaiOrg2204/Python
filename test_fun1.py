import datetime
from datetime import date

def add_num(num1,num2):
    print(num1+num2)
    return sum([num1,num2])
print(f"Sum of two digits is {add_num(5,7)}")
print(f"Sum of two digits is {add_num(6,8)}")
list1=[2,5,6,8]
list2=[5,8,9,3]
for i in range(len(list1)):
    res=add_num(list1[i],list2[i])
    print(f"Sum of {list1[i]} and {list2[i]} is {res}")
