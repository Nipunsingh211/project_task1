import random
import string
print("="*50)
print("            PASSWOD GENERATOR")
print("="*50)
length=int(input("Enter the lenght of password:"))
print("\nChoose Password Complexity")
print("1. Letters Only")
print("2. Letters + Numbers")
print("3. Letters + Numbers + Symbols")
choice=input("Enter the choice:")

if choice=="1":
  characters=string.ascii_letters
elif choice=="2":
  characters=string.ascii_letters+string.digits
elif choice=="3":
  characters=string.ascii_letters+string.digits+string.punctuation 
else:
  print("Invalid choice! Using all characters.")
  characters=string.ascii_letters+string.digits+string.punctuation
password=""
for i in range(length):
  password+=random.choice(characters)
print("="*50)
print("           Generated Password:")
print(password)
print("="*50)