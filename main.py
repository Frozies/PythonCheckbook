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
import pandas as pd


def calculateCurrentBalance(currentBalance, entryAmount):
    balance = float(currentBalance + entryAmount)
    return balance


def recalculateAllTransactions():
    ledgerCSV = loadCSV("Checking", False)

    with open(ledgerCSV) as file:
        df = pd.read_csv(file)
        saved_column = df['Entry Amount']
        newBalance = sum(saved_column)
    return newBalance

    ############################ User Input Methods ############################


def inputInteger(question):  ##### Allows Integer input that throws an error for exceptions
    while True:
        try:
            number = int(input(question))
            break
        except ValueError:
            print("No valid integer! Please try again ...")
    return number


def inputFloat(question):  ##### Allows Float input that throws an error for exceptions
    while True:
        try:
            number = float(input(question))
            break
        except ValueError:
            print("No valid Float! Please try again ...")
    return number


def inputString(question):  ##### Allows string input that throws an error for exceptions
    while True:
        try:
            string = str(input(question))
            break
        except ValueError:
            print("No valid string! Please try again ...")
    return string


def inputDate(question):  ##### Allows date input that throws an error for exceptions
    while True:
        try:
            dateString = input(question)
            if dateString == "":
                dateObject = date.today().strftime('%m/%d/%Y')
            else:
                dateObject = datetime.strptime(dateString, "%m/%d/%Y").strftime('%m/%d/%Y')
            break
        except ValueError:
            print("Incorrect format Use the format MM/DD/YYYY : ")
    return dateObject

    ############################ Load / Save CSV File ############################


def checkDir(fileName):  ### Checks the directory to see if the data folder and ledger file exists.
    directory = os.path.dirname(fileName)
    if not os.path.exists(directory):  ### If it doesn't exists, create one.
        os.makedirs(directory)


def loadCSV(inputFileName, printValues):  # file_name, dateInRangeStart, dateInRangeEnd, entries
    directory = os.path.abspath(os.path.join(os.path.curdir))
    fileName = directory + "/data/" + inputFileName + ".csv"
    checkDir(fileName)
    if not os.path.exists(fileName):
        print("File does not exist!")
        return
    if os.path.exists(fileName) & printValues is True:
        with open(fileName) as file:
            reader = csv.DictReader(file, delimiter=",") #TODO: Use Pandas
            for row in reader:
                print(row)  # TODO: Format print output better, make print ledger entries its own function
    return fileName


def saveCSV(inputFileName, entryData, fieldNames):
    directory = os.path.abspath(os.path.join(os.path.curdir))
    fileName = directory + "/data/" + inputFileName + ".csv"
    checkDir(fileName)  ### Checks for the directory
    ledgerSize = 0
    count = 0

    if os.path.exists(fileName) and os.path.isfile(fileName):
        ledgerSize = os.stat(fileName).st_size  ### Sets the var ledgerSize to see if its a new file or not.

    if ledgerSize == 0:
        with open(fileName, 'w', newline='') as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames=fieldNames) #TODO: Use Pandas
            writer.writeheader()  ### If there is no header, write one.

    for record in entryData:

        if count == len(entryData) - 1:  ### Checks to see if the current record section is the last.
            try:
                csvFile = open(fileName, 'a')
                csvFile.write('%s\n' % record)  ### Prints a new line with no comma
                csvFile.close()
            except PermissionError:
                print("Permission Error!")

        if count != len(entryData) - 1:  ### If not the last record, then write the key value with a comma
            try:
                csvFile = open(fileName, 'a')
                csvFile.write('%s,' % record)
                count += 1  ### Increase record count
                csvFile.close()
            except PermissionError:
                print("Permission Error!")
    return

    ############################ Add entry to ledger ############################


def addEntryToLedger(entryName, entryDate, entryAmount, currentBalance, ledgerFile):
    entryData = [entryName, entryAmount, entryDate]
    fieldNames = ['Entry Name', 'Entry Amount', 'Entry Date']

    saveCSV(ledgerFile, entryData, fieldNames)

    calculateCurrentBalance(currentBalance, entryAmount)

    print(entryData, " was added to the ledger!")
    return

    ############################ Create Entries ############################


def createEntry(currentBalance, ledgerFile):
    ### Asking for Input
    entryName = inputString("Please enter the entry's name: ")
    entryDate = inputDate("Please enter the entry's  or leave blank to use today's date"
                          " \nUse the format MM/DD/YYYY : ")
    entryAmount = inputFloat("Please enter an amount, use a negative for any bills: $")

    ## Save to data file
    addEntryToLedger(entryName, entryDate, entryAmount, currentBalance, ledgerFile)

    return


def createRandomEntry(currentBalance, ledgerFile):
    randomNames = ["The Polar Fiddler", "The Olive Drum", "The Bengal Drum", "The Solar Castle", "The Fire Fusion",
                   "Cinnamon", "The Nightingale", "Fantasia", "Roadhouse"]
    entryName = random.choice(randomNames)  ### Chooses a random name from the list above

    start_date = date.today().replace(day=1, month=1).toordinal()
    end_date = date.today().toordinal()  ### Picks sets today as the end date
    randomDate = date.fromordinal(random.randint(start_date, end_date))  ### Picks a random date in between
    entryDate = datetime.strptime(str(randomDate), '%Y-%m-%d').strftime('%m/%d/%Y')  ### Formats the date correctly

    entryAmount = round((random.random() * 100 + random.random()), 2)  ### Picks a random amount with decimal

    if bool(random.getrandbits(1)):  ### Randomizes to count as bill or income
        entryAmount = entryAmount * -1

    addEntryToLedger(entryName, entryDate, entryAmount, currentBalance, ledgerFile)  ### Adds entry command
    return


############################ List Entries ############################

# TODO: Create a function to list the entries in order by date

############################ Account Information ############################

# TODO: Create Income vs bill entry
# TODO: Get account balance
# TODO: Add calendar entries
# TODO: Add Repeating bills
# TODO: Categories

# TODO: Eventual Snowball planner
# TODO: Credit card account APR Planner


def main():
    Totalbalance = 0
    Totalbalance = recalculateAllTransactions()  ### On start recalculate all balances
    ledgerFile = "Checking"

    ############################ RUN / Start checking for input commands ############################

    print("\n")  # Decorative line break
    # TODO: Print a description of the program on start
    commandInput = input("Please enter a command or type help: ")

    if commandInput == "help":
        print("Command list:"
              "\naddTransaction - Adds an Entry into the checkbook",
              "\nhelp - Shows a list of commands",
              "\nrandomTransaction - Creates a random entry to input into the ledger (for debug c:)",
              "\nlistTransactions - Lists entries in ledger",
              "\nprintBalance - Prints the current balance",
              "\nrecalculateBalance - Recalculates the balance from the ledger."
              )
        return main()

    if commandInput == "addTransaction":
        createEntry(Totalbalance, ledgerFile)
        return main()

    if commandInput == "randomEntry":
        createRandomEntry(Totalbalance, ledgerFile)
        return main()

    if commandInput == "listTransactions":
        loadCSV(ledgerFile, printValues=True)
        print("Current Balance: ", Totalbalance)
        return main()

    if commandInput == "recalculateBalance":
        recalculateAllTransactions()
        print("Old Balance: ", Totalbalance)
        print("Recalculated Balance: ", recalculateAllTransactions())
        return main()

    if commandInput == "printBalance":
        print("Saved Balance: ", Totalbalance)
        return main()

    else:
        print("That is not a valid command! Please try again.")
        return main()


if __name__ == "__main__":
    main()
