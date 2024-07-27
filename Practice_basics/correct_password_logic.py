# one way with if condition

# userInput = "Enter the correct password:"
#
# correctPassword = "Nitesh@1234"
#
# while True:
#     enterPass = input(userInput)
#     if(enterPass != correctPassword):
#         print("Invalid password, please try again!")
#     else:
#         print("Correct Password, You may proceed!")
#         break


# other way without if condition
userInput = input("Enter the correct password:")

while userInput != "Nitesh@1234":
        print("Invalid password, please try again!")
        userInput = input("Enter the correct password:")


print("Correct Password, You may proceed!")