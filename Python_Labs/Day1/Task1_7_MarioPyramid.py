'''
Write a program that build a Mario pyramid like below.
'''

stone = int(input('Number of stones : '))
s = '*'

for i in range(1, stone+1):
    print(end='\n')
    print(' ' * (stone - i), s * i)
