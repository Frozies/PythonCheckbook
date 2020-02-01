###################
# Checkbook Program
# Davin Young
# Florida Gulf Coast University
# Started Jan 2020
####################
from datetime import datetime

from pip._vendor.distlib.compat import raw_input


def main():
    ############################ User Input Methods ############################

    def inputInteger(question):  ##### Allows Integer input that throws an error for exceptions
        while True:
            try:
                n = int(input(question))
                break
            except ValueError:
                print("No valid integer! Please try again ...")
        return n

    def inputFloat(question):  ##### Allows Float input that throws an error for exceptions
        while True:
            try:
                f = float(input(question))
                break
            except ValueError:
                print("No valid Float! Please try again ...")
        return f

    def inputString(question):  ##### Allows string input that throws an error for exceptions
        while True:
            try:
                s = str(input(question))
                break
            except ValueError:
                print("No valid string! Please try again ...")
        return s

    def inputDate(question):  ##### Allows date input that throws an error for exceptions
        while True:
            try:
                date_string = input(question)
                date_object = datetime.strptime(date_string, "%m/%d/%Y")
                break
            except ValueError:
                print("Incorrect format Use the format MM/DD/YYYY : ")
        return date_string

##### Broken yes or no function ####

#    def yesNoQuestion(question):
#        userInput = inputString(question)
#        try:
#            if userInput == 'y':
#                return True
#            elif userInput == 'n':
#                return False
#            else:
#                print("Invalid input please use 'y' or 'n'")
#                return yesNoQuestion(userInput)
#        except ValueError:
#            return yesNoQuestion(userInput)


############################ Book Entry ############################
    def bookEntry():

        entryName = inputString("Please enter the entry's name: ")

        #### Unused check if today's or a different date used ####
#        Date = input("Do you want to use today's date? (Enter y/n)")
#        if useDate == "y":
#            entryDate = datetime.date(datetime.now())
#        elif useDate == "n":

        entryDate = inputDate("Please enter the entry's date \nUse the format MM/DD/YYYY : ")
        entryAmount = inputFloat("Please enter an amount : $")

        return entryName, entryDate, format(entryAmount, ",.2f")
        ### Reformat the value to have a comma every 3 places, and 2 decimal points

    ############################ RUN / Start checking for input commands ############################
    print("\n")  # Decorative line break
    commandInput = input("Please enter a command or type help: ")

    while commandInput == "help":
        print("Command list:"
              "\naddEntry - Adds an Entry into the checkbook")
        return main()
    while commandInput == "addEntry":
        bookEntry()
        return main()
    else:
        print("That is not a valid command! Please try again.")
        return main()


if __name__ == "__main__":
    main()
