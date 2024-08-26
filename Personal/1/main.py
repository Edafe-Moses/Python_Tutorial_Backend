try:
    x = int(input('Input an integer: '))
    print(x)
except ValueError:
    print('Something went wrong.. Pleas try again')
finally:
    print('try except finished')