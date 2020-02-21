###################
# Checkbook Program
# Davin Young
# Florida Gulf Coast University
# Started Jan 2020
####################

### TODO: calculate current balance
# TODO: Create a function to list the entries in order by date
# TODO: Account Information
# TODO: Create Income vs bill entry
# TODO: Get account balance
# TODO: Add calendar entries
# TODO: Add Repeating bills
# TODO: Categories
# TODO: Averages
# TODO: Eventual Snowball planner
# TODO: Credit card account APR Planner
# TODO: read bank statements and ask about each transaction.

import os
from datetime import datetime, date
import csv
import random


def calculateCurrentBalance(entryAmount):
    updated_balance = 0
    updated_balance = entryAmount - getLastEntry()
    return updated_balance


def getLastEntry():
    ledger_csv = loadCSV(input_file_name="Checking", print_values=False)
    if ledger_csv:  # checks if there is a ledger csv file
        with open(ledger_csv) as file:  # opens the csv file
            reader = csv.DictReader(file, delimiter=",")  # reads the file using csv dictreader, splits data by ,
    return


def recalculateAllTransactions():  # Recalculating the transactions in the ledger to get the real balance
    ledger_csv = loadCSV(input_file_name="Checking", print_values=False)  # loads the csv file as a variable
    balance = 0  # initializes balance variable
    if ledger_csv:  # checks if there is a ledger csv file
        with open(ledger_csv) as file:  # opens the csv file
            reader = csv.DictReader(file, delimiter=",")  # reads the file using csv dictreader, splits data by ,
            entry_amount = sum(float(row['Entry Amount']) for row in reader)  # adds every item in row
        balance += entry_amount  # sets balance to the function above
    return balance


def inputInteger(question):  # Allows Integer input that throws an error for exceptions
    while True:
        try:
            number = int(input(question))
            break
        except ValueError:
            print("No valid integer! Please try again ...")
    return number


def inputFloat(question):  # Allows Float input that throws an error for exceptions
    while True:
        try:
            number = float(input(question))
            break
        except ValueError:
            print("No valid Float! Please try again ...")
    return number


def inputString(question):  # Allows string input that throws an error for exceptions
    while True:
        try:
            string = str(input(question))
            break
        except ValueError:
            print("No valid string! Please try again ...")
    return string


def inputDate(question):  # Allows date input that throws an error for exceptions
    while True:
        try:
            date_string = input(question)
            if date_string == "":
                date_object = date.today().strftime(
                    '%m/%d/%Y')  # Uses date class to get today's date in mmddyyyy format
            else:
                date_object = datetime.strptime(date_string, "%m/%d/%Y").strftime('%m/%d/%Y')  # checks formatting
            break
        except ValueError:  # checks if the format is not correct
            print("Incorrect format Use the format MM/DD/YYYY : ")
    return date_object


def checkDir(file_name):  # Checks the directory to see if the data folder and ledger file exists.
    directory = os.path.dirname(file_name)
    if not os.path.exists(directory):  ### If it doesn't exists, create one.
        os.makedirs(directory)  # creates the file but will not fill it with anything


def loadCSV(input_file_name, print_values):  # TODO: dateInRangeStart, dateInRangeEnd, entries
    directory = os.path.abspath(os.path.join(os.path.curdir))  # initializes directory to the current directory
    file_name = directory + "/data/" + input_file_name + ".csv"  # sets directory item /data/filename.csv to variable
    checkDir(file_name)  # checks if the variable file_name is a valid path
    if not os.path.exists(file_name):
        print("File does not exist!")  # if there is no file then print an error and return to main
        return
    if os.path.exists(file_name) & print_values is True:  # checks if there is a file, and if print values is true
        with open(file_name) as file:  # opens file
            reader = csv.DictReader(file)  # reads file with dict reader
            for row in reader:  # prints every row
                print(row)  # TODO: Format print output better, make print ledger entries its own function
    return file_name


def saveCSV(input_file_name, entry_data, field_names):
    directory = os.path.abspath(os.path.join(os.path.curdir))  # initializes directory to the current directory
    file_name = directory + "/data/" + input_file_name + ".csv"  # sets directory item /data/filename.csv to variable
    checkDir(file_name)  # checks if the variable file_name is a valid path
    ledger_size = 0  # initializes ledger size
    count = 0

    if os.path.exists(file_name) and os.path.isfile(file_name):
        ledger_size = os.stat(file_name).st_size  ### Sets the var ledger_size to see if its a new file or not.

    if ledger_size == 0:
        with open(file_name, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=field_names)
            writer.writeheader()  ### If there is no header, write one.

    for record in entry_data:

        if count == len(entry_data) - 1:  ### Checks to see if the current record section is the last.
            csv_file = open(file_name, 'a')
            csv_file.write('%s\n' % record)  ### Prints a new line with no comma

        if count != len(entry_data) - 1:  ### If not the last record, then write the key value with a comma
            csv_file = open(file_name, 'a')
            csv_file.write('%s,' % record)
            count += 1  ### Increase record count

        csv_file.close()
    return

    ############################ Add entry to ledger ############################


def addEntryToLedger(entry_name, entry_date, entry_amount):
    entry_data = [entry_name, entry_amount, entry_date]  # Sets up variables for ledger data based off of input
    field_names = ['Entry Name', 'Entry Amount', 'Entry Date']  # Sets up variable names for csv header

    saveCSV("Checking", entry_data, field_names)  # appends the entry data to the csv file

    # calculateCurrentBalance(entryAmount)

    print(entry_data, " was added to the ledger!")
    return

    ############################ Create Entries ############################


def createEntry():
    ### Asking for Input
    entry_name = inputString("Please enter the entry's name: ")
    entry_date = inputDate("Please enter the entry's  or leave blank to use today's date"
                           " \nUse the format MM/DD/YYYY : ")
    entry_amount = inputFloat("Please enter an amount, use a negative for any bills: $")

    ## Save to data file
    addEntryToLedger(entry_name, entry_date, entry_amount)

    return


def createRandomEntry():
    random_names = ["The Polar Fiddler", "The Olive Drum", "The Bengal Drum", "The Solar Castle", "The Fire Fusion",
                    "Cinnamon", "The Nightingale", "Fantasia", "Roadhouse"]
    entry_name = random.choice(random_names)  ### Chooses a random name from the list above

    start_date = date.today().replace(day=1, month=1).toordinal()
    end_date = date.today().toordinal()  ### Picks sets today as the end date
    random_date = date.fromordinal(random.randint(start_date, end_date))  ### Picks a random date in between
    entry_date = datetime.strptime(str(random_date), '%Y-%m-%d').strftime('%m/%d/%Y')  ### Formats the date correctly

    entry_amount = round((random.random() * 100 + random.random()), 2)  ### Picks a random amount with decimal

    if bool(random.getrandbits(1)):  ### Randomizes to count as bill or income
        entry_amount = entry_amount * -1

    addEntryToLedger(entry_name, entry_date, entry_amount)  ### Adds entry command
    return


def inputCommand(command_input, current_balance):
    if command_input == "help":
        print("Command list:"
              "\naddTransaction - Adds an Entry into the checkbook",
              "\nhelp - Shows a list of commands",
              "\nrandomTransaction - creates a random entry to input into the ledger (for debug c:)",
              "\nlistTransactions - lists entries in ledger",
              "\nprintBalance - prints the current balance",
              "\nrecalculateBalance - Recalculates all balances"
              )
    elif command_input == "addTransaction":
        createEntry()

    elif command_input == "randomTransaction":
        createRandomEntry()

    elif command_input == "listTransactions":
        loadCSV("Checking", print_values=True)

    elif command_input == "recalculateBalance":
        current_balance == recalculateAllTransactions()
        print("Current Balance: ", round(current_balance, 2))

    elif command_input == "printBalance":
        print("Current Balance: ", round(current_balance, 2))
    else:
        print("That is not a valid command! Please try again.")
    return main()


def main():
    total_balance = recalculateAllTransactions()  ### On start recalculate all balances
    getLastEntry()
    print("\n")  # Decorative line break

    command_input = input("Please enter a command or type help: ")
    inputCommand(command_input, total_balance)


if __name__ == "__main__":
    main()
