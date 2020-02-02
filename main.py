###################
# Checkbook Program
# Davin Young
# Florida Gulf Coast University
# Started Jan 2020
####################
from datetime import datetime

def main():

    Datafile = "0"

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
        return date_object

    ############################ Load/Create Data File ############################

    #ask about xlsxwriter

    def loadDataFile():


    ############################ Create Entries ############################

    def createEntry():
        ### Asking for Input
        entryName = inputString("Please enter the entry's name: ")
        entryDate = inputDate("Please enter the entry's date \nUse the format MM/DD/YYYY : ")
        entryAmount = inputFloat("Please enter an amount : $")
        return

    ############################ RUN / Start checking for input commands ############################

    print("\n")  # Decorative line break
    commandInput = input("Please enter a command or type help: ")

    while commandInput == "help":
        print("Command list:"
              "\naddEntry - Adds an Entry into the checkbook")
        return main()
    while commandInput == "addEntry":
        createEntry()
        return main()
    else:
        print("That is not a valid command! Please try again.")
        return main()


############################ Book Entry Class ############################
class BookEntry(object):

    def __init__(self, name, date, amount):
        self.name = name
        self.date = date
        self.amount = amount


if __name__ == "__main__":
    main()
