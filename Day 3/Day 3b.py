import re
import itertools

def readFile():
    with open("input", "r") as f:
        data = f.read()
        return data

def begginings(iter):
    x = []
    for a in iter:
        x.append(a.start())

    return x

#Receives object Match and returns the values of the group
def getValues(objMatch):
    start = objMatch.start()
    a = objMatch.group(1)
    b = objMatch.group(2)
    a = int(a)
    b = int(b)

    total=a*b
    return_dict = {
        "start" : start,
        "a": a,
        "b" : b,
        "mult" : total
    }

    return return_dict

data = readFile()

pattern = r"mul\((-?\d+\.?\d*),(-?\d+\.?\d*)\)"
doPattern = r"do\(\)"
dontPattern = r"don\'t\(\)"

matches_iter = re.finditer(pattern,data)
iterador1, iterador2 = itertools.tee(matches_iter, 2)
muls_list = list(iterador2)


matches = []
for match in iterador1:
    matches.append(match)

positionsDo = re.finditer(doPattern,data)
positionsDont = re.finditer(dontPattern,data)

#Location of the start of each string
dos = begginings(positionsDo)
donts = begginings(positionsDont)
muls = begginings(matches)

print("Dos: ", dos)
print("Donts: ", donts)
print("Muls: ", muls)

counterDo = 0
counterDont = 0
counter_mul = 0
total = 0
active = True


for x in range(len(data)):
    print("Valor X:",x)

    if counterDo<len(dos):
        if x == dos[counterDo]:

            active = True
            counterDo+=1
            print(f"Do encontrado en: {x}, actividad en {active}")

    if counterDont<len(donts):
        if x==donts[counterDont]:
            active = False
            counterDont+=1
            print(f"Dont encontrado en: {x}, actividad en {active}")


    if active:
        if x==muls[counter_mul]:
            valores = getValues(muls_list[counter_mul])
            total += valores["mult"]
            print(f"A:{valores["a"]} multiplicado por B: {valores["b"]} es {valores["mult"]}")


    if counter_mul<len(muls)-1:
        if x == muls[counter_mul]:
            counter_mul += 1

print(total)

