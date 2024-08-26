print("   Grading System   ")
print("--------------------")

nameArr = []
subjArr = []
avgArr = []


value = True
i = 0
j = 0

while value:
    name = input("Enter Your Name : ")
    nameArr.append(name)
    tmpArrSubj = []
    tmpAvg = 0

    while value:
        tmpArrSubj[j] = input("Enter Subject Offered : ")
        if i > 0:
            if subjArr[i][j] != tmpArrSubj[j]:
                print("Enter Correct Subject by Order")
                tmpArrSubj[j] = input("Enter Subject Offered : ")

        tmpTestOne = int(input("Enter Your 1st Test Score : "))
        if tmpTestOne > 20 or tmpTestOne < 0:
            tmpTestOne = int(input("Enter Your 1st Test Score : "))

        tmpTestTwo = int(input("Enter Your 2nd Test Score : "))
        if tmpTestTwo > 20 or tmpTestOne < 0:
            tmpTestTwo = int(input("Enter Your 1st Test Score : "))

        tmpExam = int(input("Enter Exam Score : "))
        if tmpExam > 60 or tmpTestOne < 0:
            tmpExam = int(input("Enter Your 1st Test Score : "))

        tmpAvg += tmpTestOne + tmpTestTwo + tmpExam

        v = input("Next(Enter True) or End(Enter False) : ")
        if v.lower() == "true":
            value = True
        else:
            value = False

        j = j + 1

    subjArr.append(tmpArrSubj)
    avgArr.append(tmpAvg / j)

    v = input("Next(Enter True) or End(Enter False) : ")
    if v.lower() == "true":
        value = True
    else:
        value = False

    i = i + 1
    j = 0

minimum = avgArr[0]
for c in range(1, i):
    if minimum > avgArr[c]:
        minimum = avgArr[c]
    print(minimum)