import random
import string

def generate_password(length):
    # Define the character set to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password using the defined character set
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Example usage
length = int(input("Enter the lenth of your password: "))
generated_password = generate_password(length)
print("Generated Password:", generated_password)

#Himel Sarder
#Dept. of CSE, BSFMSTU
