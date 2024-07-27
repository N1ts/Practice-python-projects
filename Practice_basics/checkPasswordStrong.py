# check 3 conditions:
# 1. password is of length 8 characters
# 2. it contains atleast 1 digit
# 3. it contains atleast 1 uppercase character

password = input("Enter the password: ")

result = {}

# condition 1 checked
if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

# condition 2 checked
digit = False
for i in password:
    if i.isdigit():
        digit = True

result["number"] = digit

# condition 3 checked
uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result["upper_case"] = uppercase


print(result)
# final logic
if all(result.values()):
    print("Strong password!")
else:
    print("Weak password!")
