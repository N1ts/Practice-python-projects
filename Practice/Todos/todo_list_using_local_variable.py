todoItems = []

def show(allItems):
    # enumerate returns index & item both of a list ex: 0 "pasta", 1 "pizza"
    for index, item in enumerate(allItems):
        print(index + 1, item)

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
            todo = input("Enter a todo item:")
            todoItems.append(todo)
        case 'show':
            show(todoItems)
        case 'edit':
            edit()
        case 'delete':
            delete()
        case 'exit':
            break

        # "_" or we can use any string like "whatever" is preferred if user types except above case texts
        case _:
            print("Incorrect value inputted!")


