def read_file(filePath="todos.txt"):
    """Read the file and returns a list of todo items"""
    with open(filePath, "r") as file:
        todos = file.readlines()
    return todos

# print(help(read_file))

def write_file(todoItems, filePath="todos.txt"):
    """Write the todo item in the text file"""
    with open(filePath, "w") as file:
        file.writelines(todoItems)

# print(help(write_file))


# this will avoid printing Hi when my main file will run, as we have used import functions in
# main file, so all the code executes there but bcz of this under if condition statement won't print
if __name__ == "__main__":
     print("Hi")