import random
password="QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm123456789!@#$%^&*?/''<>:"
length=int(input("Enter the lenght of password:"))
a="".join(random.sample(password,length))
print(f"your password is:{a}")