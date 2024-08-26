# Write a program to accept time in 24hrs format and then greet the user
name = input("Enter Your Name : ")
t = int(input("Enter Time (Hours) : "))
if 0 <= t <= 12:
    print(f"Good Morning {name}")
elif 13 <= t <= 16:
    print(f"Good Afternoon {name}")
elif 17 <= t <= 20:
    print(f"Good Evening {name}")
elif 18 <= t <= 23:
    print(f"Good Night {name}")
