'''d={"tom":173444, "ron": 1203}
tom_value=d["tom"]
d["sam"]=23443
del d["tom"]
print(d)
for key in d:
    print("key",key,"values",d[key])

d.clear()

import math
print(math.pi)
print(math.pow(2,2))

import calendar
cal=calendar.month(2025,8)
cal2=calendar.isleap(2022)
print(cal2)

import functools as f
area=f.calc(5)
print(area)
'''
import json

book = {}
book["tom"] = {
    'name': 'tom',
    'address': '123 justin,NY',
    'phone': 210200201
}
book["bob"] = {
    'name': 'bob',
    'address': 'skdfkjsdf,NY',
    'phone': 210200201
}

# Convert to JSON string
s = json.dumps(book)
print(s)

# Fix 1: Use raw string (r prefix) for file path
file_path = r"D:\Users\RODELAA\vsPython\.vscode\book.txt"

# Write to file
with open(file_path, "w") as f:
    f.write(s)

# Read back from file
with open(file_path, "r") as f:
    content = f.read()
    print("Content read from file:")
    print(content)