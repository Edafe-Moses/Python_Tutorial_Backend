print("Calculator App")
print("--------------")

f = float(input("Enter the First Number : "))
s = float(input("Enter the Second Number : "))
sign = input("Enter Operation being Carried Out")

if sign == '+':
    print(f"{f} + {s} = {f + s}")
elif sign == '-':
    print(f"{f} - {s} = {f - s}")
elif sign == '/':
    print(f"{f} / {s} = {f / s}")
elif sign == '*':
    print(f"{f} * {s} = {f * s}")
else:
    print("Invalid Operation")