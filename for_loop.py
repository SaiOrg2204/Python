dict1={
    "key1": "Toys",
    "Key2": "Cars",
    "Key3": "Bikes",
    "Key4": "Flights"
}
a = [12,23,34,45,56,67,78,89,90]
print(dict1)
for k,v in dict1.items():
    print(f"Given key {k} -----> {v}")
print(enumerate(dict1))
for i, item in enumerate(a, start=1):
    print(f"Index number is {i} and item is {item} and it's address is {id(item)} and address of list a is {id(a)}")

for i, (k,v) in enumerate(dict1.items(), start=1):
    print(f"Index of the current iteration is {i} and key is {k} and value is {v}")

for item in range(len(a)):
    print(f"Item from list is {a[item]}")

for item in a:
    print(f"current item from the list is {item}")
