
#Checks if the given list is always increasing or decreasing
#Also returns false if two consecutive numbers are the same, (no decrease nor increase)
def checkList(lista):

    #check for strictly increasing list
    inc = all(i < j for i, j in zip(lista, lista[1:]))

    #check for strictly decreasing list
    dec = all(i>j for i,j in zip(lista,lista[1:]))

    if inc == True or dec == True:
        return True
    else:
        return False

numbers=[]
with open("input", "r") as f:
    for line in f:
        numbers.append(line.split())

for i in range(len(numbers)):  # Iterate through rows
    for j in range(len(numbers[i])):  # Iterate through columns in each row
        numbers[i][j] = int(numbers[i][j])

safe = 0
for i in range(len(numbers)):  # Iterate through rows
    if checkList(numbers[i]): #We only want to iterate through the arrays that are either ascending or descending
        print(f"{numbers[i]}")
        for j in range(len(numbers[i])-1):  # Iterate through columns in each row
            r = abs(numbers[i][j+1]-numbers[i][j])
            print(r)
            if r > 3:
                break
            if r==0:
                break;
            if j==len(numbers[i])-2:
                safe += 1
                print("--------------------")


print(f"Safe: {safe}")




