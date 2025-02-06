from itertools import combinations

def checkList(arr):
    safeList=[]
    ans = 0
    for array in combinations(arr, len(arr)-1):

        safepos = set([1, 2, 3])
        safeneg = set([-1, -2, -3])
        for i in range(1, len(array)):
            safepos.add(array[i] - array[i - 1])
            safeneg.add(array[i] - array[i - 1])

        print(f"array: {array} set valuepos: {safepos} valueneg{safeneg}")

        if len(safepos) == 3 or len(safeneg) == 3:
           return True


# Lista original
with open("input", "r") as f:
    content = f.read().strip().split("\n")

safe = 0

for report in content:
    values = list(map(int,report.split()))
    if checkList(values) == True:
        safe+=1
        print("...........................")

print(safe)


