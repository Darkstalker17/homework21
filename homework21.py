import random
import string
combined_list = list(string.ascii_letters + string.digits)
length = int(input("Enter how many characters long you want your password to be : "))
password = ""
for i in range(length):
    password = password + random.choice(combined_list)
print(password)

             
