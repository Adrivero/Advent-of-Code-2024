
d=[]

with open("data.txt","r") as fichero:
    a=[]
    b=[]
    for line in fichero:
        p = line.split()

        a.append(int(p[0]))
        b.append(int(p[1]))

a.sort()
b.sort()


for c in range(1000):
    d.append(abs(b[c]-a[c]))

print(f"First part: {sum(d)}")



score=0
coincidences=0
for x in range(len(a)):
    for y in range(len(b)):
         if a[x]==b[y]:
            coincidences +=1

    score = score + a[x]*coincidences
    coincidences=0

print(score)
