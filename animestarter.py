import webbrowser
import os
import pathlib

# gets the directory the software is located in and
directory = os.getcwd() + "\Files"
# Todo: should clear the console not working yet
clearConsole = lambda: os.system('cls')


# if the Files directory doesn't exist it creates one
def createFileDirectory():
    pathlib.Path(directory).mkdir(parents=True, exist_ok=True)


# get all files in a list
def getFiles():
    return os.listdir(directory)


# reads in the input which file should be used
def getFileInput():
    while True:
        try:
            number = int(input("Enter a number from 1 to " + str(len(getFiles())) + ": "))
            # if number > getFiles() or number < 1:
            if not 1 <= number <= len(getFiles()):
                raise ValueError
            else:
                return number
        except ValueError:
            print("Sorry, I didn't understand that.")
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


# removes a file
def removeFile():
    printFiles()
    fileinput = input("Enter a file name that u want to remove : ")
    if fileinput != "":
        path = os.path.join(directory, fileinput)
        try:
            os.remove(path)
        except FileNotFoundError:
            print('Failed removing the file')
        else:
            print('File removed')


# opens all Links
def openLinks():
    number = getFileInput()
    if number == 1:
        # Finished Anime
        print("1")
    if number == 2:
        # Waiting for new episodes
        print("2")
    if number == 3:
        # Episodes exist
        print("3")
    if number == 4:
        # Anime to Watch
        print("4")


# displays all options
def displayOptions():
    print("1 Create File | 2 Remove File | 3 Show Files | 4 Open File")


# reads in the execute option which is selected
def chooseExecuteOptions():
    while True:
        try:
            number = int(input("Enter a number from 1 to 4: "))
            if not 1 <= number <= 4:
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
        openLinks()


# def execute(chosenExecuteOptions):
#     match chosenExecuteOptions:
#         case "1":
#             createNewFile()
#         case "2":
#             removeFile()
#         case "3":
#             printFiles()
#         case "4":
#             openLinks()


# main method which executes all methods
def main():
    createFileDirectory()
    displayOptions()
    chosenExecuteOptions = chooseExecuteOptions()
    execute(chosenExecuteOptions)


if __name__ == "__main__":
    main()
