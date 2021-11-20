import webbrowser
import os


def getFiles():
    return os.listdir(os.getcwd() + "\Files")


def getInput():
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
            # better try again... Return to the start of the loop
            continue


def printFiles():
    for i, j in zip(getFiles(), range(len(getFiles()))):
        print(str(j + 1) + " " + i)


def main():
    printFiles()
    number = getInput()
    if number == 1:
        # Finished Animes
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


if __name__ == "__main__":
    main()
