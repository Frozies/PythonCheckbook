###################
# Checkbook Program
# Davin Young
# Florida Gulf Coast University
# Started Jan 2020
####################
import os
from datetime import datetime, date
import csv
import random


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
                dateString = input(question)
                dateObject = datetime.strptime(dateString, "%m/%d/%Y")
                break
            except ValueError:
                print("Incorrect format Use the format MM/DD/YYYY : ")
        return dateObject

    ############################ Save CSV File ############################
    def checkDir(fileName):  ### Checks the directory to see if the data folder and ledger file exists.
        directory = os.path.dirname(fileName)
        if not os.path.exists(directory):  ### If it doesn't exists, create one.
            os.makedirs(directory)

    def saveCSV(fileName, entryData, fieldNames):
        checkDir(fileName)  ### Checks for the directory
        ledgerSize = 0
        count = 0

        if os.path.exists(fileName) and os.path.isfile(fileName):
            ledgerSize = os.stat(fileName).st_size  ### Sets the var ledgerSize to see if its a new file or not.

        if ledgerSize == 0:
            with open(fileName, 'w', newline='') as csvFile:
                writer = csv.DictWriter(csvFile, fieldnames=fieldNames)
                writer.writeheader()  ### If there is no header, write one.

        for record in entryData:

            if count == len(entryData) - 1:  ### Checks to see if the current record section is the last.
                csvFile = open(fileName, 'a')
                csvFile.write('%s\n' % record)  ### Prints a new line with no comma

            if count != len(entryData) - 1:  ### If not the last record, then write the key value with a comma
                csvFile = open(fileName, 'a')
                csvFile.write('%s,' % record)
                count += 1  ### Increase record count

            csvFile.close()
        return

    ############################ Add entry to ledger ############################
    def addEntryToLedger(entryName, entryDate, entryAmount):
        entryData = [entryName, entryAmount, entryDate]
        fieldNames = ['Entry Name', 'Entry Amount', 'Entry Date']
        directory = os.path.abspath(os.path.join(os.path.curdir))
        saveCSV(directory + "/data/Ledger.csv", entryData, fieldNames)

        print(entryData, " was added to the ledger!")
        return

    ############################ Create Entries ############################

    def createEntry():
        ### Asking for Input
        entryName = inputString("Please enter the entry's name: ")
        entryDate = inputDate("Please enter the entry's date \nUse the format MM/DD/YYYY : ")
        # TODO: Ask for today's date
        entryAmount = inputFloat("Please enter an amount : $")

        ## Save to data file
        addEntryToLedger(entryName, entryDate, entryAmount)

        return

    def createRandomEntry():
        randomNames = ["The Polar Fiddler", "The Olive Drum", "The Bengal Drum", "The Solar Castle", "The Fire Fusion",
                       "Cinnamon", "The Nightingale", "Fantasia", "Roadhouse"]
        entryName = random.choice(randomNames)  ### Chooses a random name from the list above

        start_date = date.today().replace(day=1, month=1).toordinal()
        end_date = date.today().toordinal()  ### Picks sets today as the end date
        randomDate = date.fromordinal(random.randint(start_date, end_date))  ### Picks a random date in between
        entryDate = datetime.strptime(str(randomDate), '%Y-%m-%d').strftime('%m/%d/%Y')  ### Formats the date correctly

        entryAmount = round((random.random() * 100 + random.random()), 2)  ### Picks a random amount with decimal

        addEntryToLedger(entryName, entryDate, entryAmount)  ### Adds entry command
        return

    ############################ List Entries ############################

    # TODO: Create a function to list the entries in order by date

    ############################ Account Information ############################

    # TODO: Create Income vs bill entry
    # TODO: Get account balance
    # TODO: Add calendar entries
    # TODO: Add Repeating bills

    # TODO: Eventual Snowball planner
    # TODO: Credit card account APR Planner

    ############################ RUN / Start checking for input commands ############################

    print("\n")  # Decorative line break
    commandInput = input("Please enter a command or type help: ")

    while commandInput == "help":
        print("Command list:"
              "\naddEntry - Adds an Entry into the checkbook",
              "\nhelp - Shows a list of commands",
              "\nrandomEntry - creates a random entry to input into the ledger (for debug c:)")
        return main()
    while commandInput == "addEntry":
        createEntry()
        return main()
    while commandInput == "randomEntry":
        createRandomEntry()
        return main()
    else:
        print("That is not a valid command! Please try again.")
        return main()


if __name__ == "__main__":
    main()
