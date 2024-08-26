n = int(input("Enter Number of times to Input a value : "))  # number of times to input a value
avgArr = []  # array to store values entered

for i in range(n):
    avgArr.append(int(input(f"Enter Value {i + 1} : ")))

maxi = avgArr[0]
for i in range(1, n):
    if maxi < avgArr[i]:
        maxi = avgArr[i]
print(maxi)
