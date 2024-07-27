import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    userAction = input("Type add, show, edit, delete or exit:") + "\n"
    userAction = userAction.strip()

    if userAction.startswith("add"):
        # slicing "add " from userAction
        todo = userAction[4:] + "\n"

        # read todos from file
        todoItems = functions.read_file()
        todoItems.append(todo)

        # write todos to file
        functions.write_file(todoItems)

    elif userAction.startswith("show"):
        todoItems = functions.read_file("todos.txt")
        for index, item in enumerate(todoItems):
            # removed extra space "\n" inside the same loop
            item = item.strip("\n")
            print(index + 1, item)

    elif userAction.startswith("edit"):
        try:
            editUserAction = userAction[5:]
            # edit(editUserAction)
            editPos = int(editUserAction)
            editPos = editPos - 1
            editText= input("Edit todo item:") + "\n"
            todoItems = functions.read_file()
            todoItems[editPos] = editText
            functions.write_file(todoItems)
            print("Text editted!!")
        except ValueError:
            print("Enter a number after edit!")
            continue

    elif userAction.startswith("delete"):
        try:
            deleteUserAction = userAction[7:]
        # delete(deleteUserAction)
            deletePos = int(deleteUserAction)
            deletePos = deletePos - 1
            todoItems = functions.read_file()
            todoItems.pop(deletePos)
            functions.write_file(todoItems)
        except ValueError:
            print("Enter a number after delete!")
            continue

    elif userAction.startswith("exit"):
        break

    else:
        print("Command is not valid!")


