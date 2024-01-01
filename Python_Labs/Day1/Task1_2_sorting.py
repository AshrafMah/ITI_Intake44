'''Fill an array of 5 elements from the user, Sort it in descending
and ascending orders then display the output.'''

elements = []

for i in range(5):
    elements.append(input(f'element {i+1}: '))
'''
elements.append(input('element1: '))
elements.append(input('element2: '))
elements.append(input('element3: '))
elements.append(input('element4: '))
elements.append(input('element5: '))
'''

elements.sort()
print("Ascending Order: ",elements)

elements.sort(reverse=True)
print("Desending Order: ",elements)

