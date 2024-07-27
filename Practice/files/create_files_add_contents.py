contents = ["a doc is important", "report will be found after the work done", "it is provided in a ppt file"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

# ZIP is a method to merge two list together it creates a format like [(item0,item0), (item1,item1), (item2,item2)]
# where (0,0) is denoted to 1st item of both lists
for i,j in zip(filenames, contents):
    file = open(i, "w")
    file.writelines(j)
    file.close()
    print(i)
