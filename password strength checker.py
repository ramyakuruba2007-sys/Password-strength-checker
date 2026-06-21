# Password strength checker
password=input("Enter your password: ")
length=len(password)
if length<6:
    print("Weak password")
elif length>=6 and length<10:
    print("Medium password")
else:
    print("Strong password")
    