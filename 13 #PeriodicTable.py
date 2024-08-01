# pip install periodictable

import periodictable

Atomic_NO = int(input("Enter Element Atomic No: "))
    
element = periodictable.elements[Atomic_NO]

print("Atomic Number : ", element.number)
print("Symbol : ", element.symbol)
print("Name : ", element.name)
print("Atomic mass : ", element.mass)
print("Density : ", element.density)

# Himel Sarder
# Dept. of CSE, BSFMSTU
