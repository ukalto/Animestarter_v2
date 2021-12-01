import webbrowser
import os
import pathlib

# gets the directory the software is located in and
directory = os.getcwd() + "\Files"
# Todo: should clear the console not working yet
clearConsole = lambda: os.system('cls')
options = 5


# if the Files directory doesn't exist it creates one
def createFileDirectory():
    pathlib.Path(directory).mkdir(parents=True, exist_ok=True)


# get all files in a list
def getFiles():
    return os.listdir(directory)


# gets a file by its index
def getFileByNumber(number):
    list1 = getFiles()
    return list1[number - 1]


# reads in the input which file should be used and opens the links
def getFileInput():
    printFiles()
    while True:
        try:
            inputnf = input("Enter a number from 1 to " + str(len(getFiles())) + " or the filename: ")
            # if number > getFiles() or number < 1:
            if not checkFiles(inputnf) and not 1 <= int(inputnf) <= len(getFiles()):
                raise ValueError
            else:
                return inputnf
        except ValueError:
            print("This File does not exist.")
            continue


# print all filenames which are in the Files directory
def printFiles():
    for i, j in zip(getFiles(), range(len(getFiles()))):
        print(str(j + 1) + " " + i)


# creates an empty file in the Files directory
def createNewFile():
    fileinput = input("Enter a file name: ")
    if fileinput != "":
        file = os.path.join(directory, fileinput)
        try:
            open(file, 'a').close()
        except OSError:
            print('Failed creating the file')
        else:
            print('File created')


# checks if a File exists with certain String
def checkFiles(checkString):
    return getFiles().__contains__(checkString)


# removes a file
def removeFile():
    printFiles()
    fileinput = input("Enter a number from 1 to " + str(len(getFiles())) + " or the filename you want to remove: ")
    if fileinput != "":
        if (checkFiles(fileinput)):
            path = os.path.join(directory, fileinput)
        else:
            file = getFileByNumber(int(fileinput))
            path = os.path.join(directory, file)
        try:
            os.remove(path)
        except FileNotFoundError:
            print('Failed removing the file')
        else:
            print('File removed')


# opens all Links with a given filename
def openLinks(inputnf):
    filename = inputnf
    if not checkFiles(filename):
        filename = getFileByNumber(int(inputnf))
    path = os.path.join(directory, filename)
    file1 = open(path, 'r')
    lines = file1.readlines()
    for i in lines:
        webbrowser.open(i.strip())


# Todo: No working completely
# checks the given file if the word is in one of the links
def checkFile(file, word):
    path = os.path.join(directory, file)
    file1 = open(path, 'r')
    lines = file1.readlines()
    for i in lines:
        if i.__contains__(word):
            return True

# Todo: No working completely
# goes through all Files and calls the checkFile method
def checkLinkExists():
    word = input("Enter a significant word which you want to search for: ")
    list1 = getFiles()
    for i in list1:
        if checkFile(i, word):
            return i


# Todo: Another Option: Move Link from one file to another file
# displays all options
def displayOptions():
    print("1 Create File | 2 Remove File | 3 Show Files | 4 Open File | 5 Check Link exists")


# reads in the execute option which is selected
def chooseExecuteOptions():
    while True:
        try:
            number = int(input("Enter a number from 1-" + str(options) + " to choose your option: "))
            if not 1 <= number <= options:
                raise ValueError
            else:
                return number
        except ValueError:
            print("No valid input. Please enter a valid number.")
            continue


# executes the option
def execute(chosenExecuteOptions):
    if chosenExecuteOptions == 1:
        createNewFile()
    if chosenExecuteOptions == 2:
        removeFile()
    if chosenExecuteOptions == 3:
        printFiles()
    if chosenExecuteOptions == 4:
        openLinks(getFileInput())
    if chosenExecuteOptions == 5:
        checkLinkExists()


# main method which executes all methods
def main():
    createFileDirectory()
    while True:
        displayOptions()
        execute(chooseExecuteOptions())


if __name__ == "__main__":
    main()
