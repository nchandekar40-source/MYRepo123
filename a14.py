# 1. Input/output functions in python
# print() - output and input() – data entry function 
# vol = 3.14  (rad * rad*) * ht
Rad = float(input('Enter Radius : '))
ht = float(input ('Enter Height : '))

vol = 3.14 * (Rad * Rad) * ht
print(f'Radius = {Rad} Height = {ht} Volume = {vol}')

