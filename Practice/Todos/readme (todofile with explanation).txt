def edit():
    editPos = int(input("Type number of the todo item to edit:"))
    editPos = editPos - 1
    editText= input("Edit todo item:")
    todoItems[editPos] = editText
    print("Text editted!!")

def delete():
    deletePos = int(input("Type number of the todo item to delete:"))
    deletePos = deletePos - 1
    todoItems.pop(deletePos)


while True:
    userAction = input("Type add, show, edit, delete or exit:")

    #match case used to check entered input by user ex: add, show, edit,  delete, exit
    match userAction.strip():
        case 'add':
            todo = input("Enter a todo item:") + "\n"
            file = open("../todos.txt", "r")
            #readlines creates a list, we stored it in todoItems variable
            todoItems = file.readlines()
            file.close()

            # Performed operation on the stored list variable
            todoItems.append(todo)
            print(todoItems)

            # we are writing on the existing file with todoItems list available, it will override the existing file
            file = open("../todos.txt", "w")
            file.writelines(todoItems)
            file.close()
        case 'show':
            file = open("../todos.txt", "r")
            showTodos = file.readlines()
            file.close()

            # removed extra space "\n" using for loop
            # newShowTodos = []
            # for removeExtraSpace in showTodos:
            #     removedSpace = removeExtraSpace.strip("\n")
            #     newShowTodos.append(removedSpace)
            # print(newShowTodos)

            #removed extra space "\n" using list comprehension, here the operation we will perform in the for loop we write
            # .. first and then the loop statement later, and assinged to new list newShowTodos, all in one line
            # newShowTodos = [removeExtraSpace.strip("\n") for removeExtraSpace in showTodos]

            # Enumerate is a method to get the index and item of a list, it creates a format like [(index0,item0), (index1,item1), (index2,item2)]
            # where (0,0) is denoted to an index and an item of the list
            for index, item in enumerate(showTodos):
                # removed extra space "\n" inside the same loop
                item = item.strip("\n")
                print(index + 1, item)

        case 'edit':
            edit()
        case 'delete':
            delete()
        case 'exit':
            break

        # "_" or we can use any string like "whatever" is preferred if user types except above case texts
        case _:
            print("Incorrect value inputted!")


