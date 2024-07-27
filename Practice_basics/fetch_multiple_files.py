# glob module provides the pathnames in the form of list

import glob

# provided a file path
myfiles = glob.glob("files_to_fetch/*.txt")
print(myfiles)

# iterate through each file and read the content
for filepath in myfiles:
    with open(filepath, "r") as file:
        print(file.read())