#Ex1:
age = int(input("Enter age: "))
# twenty
# ValueError: invalid literal for int() with base 10: 'twenty'

#Ex2:
premium = int(input("Enter premium amount: "))

print("Premium:", premium)
#2000 - correct
#abc- ValueError


#try and except
try:
    premium = int(input("Enter premium amount: "))
    print("Premium:", premium)

except:
    print("Invalid premium amount.")

#-- Enter premium amount: abc
#Invalid premium amount.