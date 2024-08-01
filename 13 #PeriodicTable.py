import periodictable

try:
    Atomic_NO = int(input("Enter Element Atomic No: "))
    if Atomic_NO <= 0 or Atomic_NO > len(periodictable.elements):
        raise ValueError("Invalid atomic number.")
    
    element = periodictable.elements[Atomic_NO]

    print("Atomic Number : ", element.number)
    print("Symbol : ", element.symbol)
    print("Name : ", element.name)
    print("Atomic mass : ", element.mass)
    print("Density : ", element.density)

except ValueError:
    print("Error: Invalid input. Please enter a valid atomic number.")
except KeyError:
    print("Error: Element with the provided atomic number does not exist.")
except:
    print("An unexpected error occurred.")

# Himel Sarder
# Dept. of CSE, BSFMSTU
