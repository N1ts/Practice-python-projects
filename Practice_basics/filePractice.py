userInput = input("Enter the text:") + "\n"

# it opens the file, then returns a list,we have hold it in a variable..
# .. later we performed an operation over this list (append), and this adds a newly text below to the existing one
file = open("../Practice/practiceFile.txt", "r")
todos = file.readlines()
file.close()

# append will add new text below to the existing one in the file and now todos variable have all the file texts
todos.append(userInput)



# writelines method is used to write texts in a file but if we directly use it, it will override the text...
# ..instead adding a new text below previous text so use readlines method prior to this to read from file...
# ..then writelines will override the complete file and add a new text below it
# writelines & readlines work converts text in list whereas write and read keeps text to string format
file = open("../Practice/practiceFile.txt", "w")
file.writelines(todos)
file.close()