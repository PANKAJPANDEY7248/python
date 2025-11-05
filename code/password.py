import random

print("🔐 Welcome to the Password Generator!")

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?/"

length = int(input("Enter the desired password length: "))

password = []


for i in range(length):

    password.append(random.choice(characters))


final_password = ''.join(password)

print(f"Your secure password is: {final_password}")
