# count = 1
# while count<=6:
#     print(count)
#     count +=1

# test = [1,2,3, "text"]
#
# for i in test:
#     print(type(test.index(2)))
#     print(i)

menu = ["pasta", "pizza", "salad"]

user_choice = (input("Enter the index of the item: ")) + "\n"


for index, item in enumerate(menu):

    match menu:
        case 0:
            message = f"You chose {index}-{menu[user_choice]}."
            print(message)
            break

        case 1:
            message = f"You chose {index}-{menu[user_choice]}."
            print(message)
            break

print("out")

file = open("../Practice/Todos/todos.txt", "r")
todos = file.readlines()
print(type(todos))
todos.append(user_choice)
file = open("../Practice/Todos/todos.txt", "w")
file.writelines(todos)


