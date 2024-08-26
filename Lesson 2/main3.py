n = int(input("Enter Amount of Values being Computed : "))
avgArr = []

for i in range(n):
    avgArr.append(int(input(f"Enter Value {i + 1} : ")))


for i in range(n):
    for j in range(i+1, n):
        if avgArr[i] > avgArr[j]:
            tmpArr = avgArr[j]
            avgArr[j] = avgArr[i]
            avgArr[i] = tmpArr


print(avgArr)