# 3.File Reader Class
# Task: Implement a FileReader class that takes a file path and
# provides methods to read the file line by line or all at once.
# Example Input: reader = FileReader(“file.txt”); reader.read_line()
# Example Output: “First line of file.”

class FileReader:
    def __init__(self, path):
        self.path = path

    def read_line_by_line(self, n):
        # r - access mode
        file = open(self.path, "r")
        count = 0
        for line in file:
            print(line)
            count += 1
            if count == n:
                file.close()
                break
                
    def read_all(self):
        file = open(self.path, "r")
        print(file.read())
        file.close()


readFile = input("Enter the file path you wish to read from: ")

newFile = FileReader(readFile)

command = input("Would you like to read all or read line by line: ")

if command == "read all":
    newFile.read_all()
elif command == "read line by line":
    numberOfLines = input("Enter the number of lines you wish to read: ")
    newFile.read_line_by_line(int(numberOfLines))
else:
    print("No such command!")
    exit()



