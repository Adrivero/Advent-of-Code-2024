import re

def readFile():
    with open("input", "r") as f:
        data = f.read()
        return data

data = readFile()

pattern = r"mul\((-?\d+\.?\d*),(-?\d+\.?\d*)\)"
matches = re.findall(pattern, data)

total = 0
for match in matches:

    a,b=match
    a = int(a)
    b = int(b)
    x = a*b
    total+=x

print(total)



