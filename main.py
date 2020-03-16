###################
# Checkbook Program
# Davin Young
# Florida Gulf Coast University
# Started Jan 2020
####################
import math
import os
from datetime import datetime, date, timedelta
import csv
import random


def getLastEntryAmount(file_path):
    checkLedgerPath(file_path=file_path)

    file_name = loadCSV(input_file_name='Checking', print_values=False)

    with open(file_name) as file:  # opens file
        reader = csv.reader(file)  # reads file with dict reader
        row_index = 4  # pick what row you want
        data = [row for row in reader]  # sets the list data to a variable
        data_reversed = data[::-1]  # slice - No value before or after the first colon and increment by -1
        column_data = [row[row_index] for row in data_reversed]  # chooses a column based on the number you pick
        retrieved_data = column_data[0]  # picks the first values
    return retrieved_data


def recalculateAllTransactions():  # Recalculating the transactions in the ledger to get the real balance
    ledger_path = loadCSV(input_file_name="Checking", print_values=False)  # loads the csv file as a variable
    balance = 0  # initializes balance variable
    if ledger_path:  # checks if there is a ledger csv file
        with open(ledger_path) as file:  # opens the csv file
            reader = csv.DictReader(file, delimiter=",")  # reads the file using csv dictreader, splits data by ,
            entry_amount = sum(float(row['Entry Amount']) for row in reader)  # adds every item in row
        balance += entry_amount  # sets balance to the function above
    last_entry_balance = getLastEntryAmount(ledger_path)
    if balance == last_entry_balance:
        print("Balance was correct")
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
                date_object = date.today().strftime('%m/%d/%Y')  # Uses date class to get
                # today's date in mmddyyyy format
            else:
                date_object = datetime.strptime(date_string, "%m/%d/%Y").strftime('%m/%d/%Y')  # checks formatting
            break
        except ValueError:  # checks if the format is not correct
            print("Incorrect format Use the format MM/DD/YYYY : ")
    return date_object


def checkLedgerPath(file_path):  # Checks the directory to see if the data folder and ledger file exists.
    directory = os.path.dirname(file_path)
    ledger_size = 0
    field_names = ['Entry Name', 'Entry Amount', 'Entry Date', 'Category',
                   'Current Balance']  # Sets up variable names for csv header

    if not os.path.exists(directory):  ### If it doesn't exists, create one.
        os.makedirs(directory)  # creates the folder  but will not fill it with anything

    try:
        ledger_size = os.stat(file_path).st_size  ### Sets the var ledger_size to see if its a new file or not.
    except FileNotFoundError:
        open(file_path, 'x')

    if ledger_size == 0:
        writeDataToCSV(file_path=file_path, entry_data=field_names)

    return


def loadCSV(input_file_name, print_values):  # TODO: dateInRangeStart, dateInRangeEnd, entries

    directory = os.path.abspath(os.path.join(os.path.curdir))  # initializes directory to the current directory
    file_path = directory + "/data/" + input_file_name + ".csv"  # sets directory item /data/filename.csv to variable
    checkLedgerPath(file_path)  # checks if the variable file_name is a valid path

    if os.path.exists(file_path) & print_values is True:  # checks if there is a file, and if print values is true
        with open(file_path) as file:  # opens file
            reader = csv.DictReader(file)  # reads file with dict readerkk
            for row in reader:  # prints every row
                print("row:"+ row + ".")

    return file_path


def saveCSV(input_file_name, entry_data):
    directory = os.path.abspath(os.path.join(os.path.curdir))  # initializes directory to the current directory
    file_path = directory + "/data/" + input_file_name + ".csv"  # sets directory item /data/filename.csv to variable
    checkLedgerPath(file_path)  # checks if the variable file_name is a valid path

    entry_amount = entry_data[1]
    if not getLastEntryAmount(file_path=file_path) == "Current Balance":
        current_balance = round(float(entry_amount) + float(getLastEntryAmount(file_path=file_path)), 2)
    else:
        current_balance = entry_amount
    entry_data.append(float(current_balance))

    writeDataToCSV(file_path=file_path, entry_data=entry_data)
    return


def writeDataToCSV(file_path, entry_data):
    count = 0
    # This fills in data like a type writer
    for record in entry_data:

        if count == len(entry_data) - 1:  ### Checks to see if the current record section is the last.
            csvFile = open(file_path, 'a')
            csvFile.write('%s\n' % record)  ### Prints a new line with no comma

        if count != len(entry_data) - 1:  ### If not the last record, then write the key value with a comma
            csvFile = open(file_path, 'a')
            csvFile.write('%s,' % record)
            count += 1  ### Increase record count

        csvFile.close()
    return


def addEntryToLedger(entry_name, entry_date, entry_amount, category_index):
    entry_data = [entry_name, entry_amount, entry_date,
                  category_index]  # Sets up variables for ledger data based off of input

    saveCSV("Checking", entry_data)  # appends the entry data to the csv file

    print(entry_data, " was added to the ledger!")
    return


def createEntry():
    ### Asking for Input
    entry_name = inputString("Please enter the entry's name: ")
    entry_date = inputDate("Please enter the entry's  or leave blank to use today's date" +
                           "\nUse the format MM/DD/YYYY : ")
    entry_amount = inputFloat("Please enter an amount, use a negative for any bills: $")

    listCategory()
    category_index = inputInteger("\nPlease select a category by typing it's number: ")
    directory = os.path.abspath(os.path.join(os.path.curdir))  # initializes directory to the current directory
    file_path = directory + "/data/Categories.config"  # sets directory item /data/filename.csv to variable
    cat_list = [line.rstrip('\n') for line in open(file_path)]

    ## Save to data file
    addEntryToLedger(entry_name, entry_date, entry_amount, cat_list[category_index])

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

    checkCategoryPath()
    directory = os.path.abspath(os.path.join(os.path.curdir))  # initializes directory to the current directory
    file_path = directory + "/data/Categories.config"  # sets directory item /data/filename.csv to variable
    cat_list = [line.rstrip('\n') for line in open(file_path)]
    random_category_index = round(random.random() * len(cat_list))

    addEntryToLedger(entry_name, entry_date, entry_amount, cat_list[random_category_index])  ### Adds entry command
    return


def saveCategory(entry_data):
    directory = os.path.abspath(os.path.join(os.path.curdir))  # initializes directory to the current directory
    file_path = directory + "/data/Categories.config"  # sets directory item /data/filename.csv to variable

    checkCategoryPath()

    with open(file_path, 'a') as file:
        file.write(str(entry_data) + "\n")

    return


def checkCategoryPath():
    directory = os.path.abspath(os.path.join(os.path.curdir))  # initializes directory to the current directory
    file_path = directory + "/data/Categories.config"  # sets directory item /data/filename.csv to variable
    ledger_size = 0

    default_categories = 'No Category\n' \
                         'Income\n' \
                         'Groceries\n' \
                         'Housing\n' \
                         'Transportation\n' \
                         'Food\n' \
                         'Utilities\n' \
                         'Insurance\n' \
                         'Medical\n' \
                         'Savings\n' \
                         'Entertainment\n'

    if not os.path.exists(directory):  ### If it doesn't exists, create one.
        os.makedirs(directory)  # creates the folder  but will not fill it with anything

    try:
        ledger_size = os.stat(file_path).st_size  ### Sets the var ledger_size to see if its a new file or not.
    except FileNotFoundError:
        open(file_path, 'x')

    if ledger_size == 0:
        with open(file_path, 'a') as file:
            file.write(default_categories)

    return


def listCategory():
    checkCategoryPath()
    directory = os.path.abspath(os.path.join(os.path.curdir))  # initializes directory to the current directory
    file_path = directory + "/data/Categories.config"  # sets directory item /data/filename.csv to variable
    count = 0

    cat_list = [line.rstrip('\n') for line in open(file_path)]

    for x in range(math.ceil(len(cat_list) / 3)):  # ceiling(categories index / 3)
        for y in range(3):
            if count <= (len(cat_list) - 1):
                print(str(count) + ".) " + str(cat_list[count]) + " ", end=" ")
                count += 1
        print()
    return


def sumCategories(active_ledger):
    # date_range = today's date - 30 days

    # read data from ledger file, active_ledger
    # reverse list
    # check if the date is in range with date_range
    # retrieve category text and compare to category config
    # if the category doesnt exist, add it to the config
    # skip if length == index or length - 1 == index (first and 2nd default entries skipped)
    # make a new list with the length of categories config
    # add the current transaction to this list
    # once done print data
    #
    #   This month's Spending
    #   Food: $153.31
    #   Gas: $204.45
    #   Rent: $800.00
    #   Entertainment: $103.22

    start_date = (date.today() - timedelta(days=30)).toordinal()
    end_date = date.today().toordinal()
    cat_sums = []
    ledger_path = loadCSV(input_file_name=active_ledger, print_values=False)

    with open(ledger_path) as file:  # opens file
        row_index = 3  # pick what row you want
        reader = csv.reader(file)  # reads file with dict reader
        data = [row for row in reader]  # sets the list data to a variable
        data_reversed = data[::-1]  # slice - No value before or after the first colon and increment by -1

        print(delta_date)

        for i in data_reversed:
            print("sum cat: " + str(i))


        #column_data = [row[row_index] for row in data_reversed]  # chooses a column based on the number you pick
        #retrieved_data = column_data[0]  # picks the first values #index



    return


def inputCommand(command_input, active_ledger):
    print() # Decorative Print
    current_balance = float(0)

    directory = os.path.abspath(os.path.join(os.path.curdir))  # initializes directory to the current directory
    file_path = directory + "/data/" + active_ledger + ".csv"  # sets directory item /data/filename.csv to variable

    if command_input == "help":
        print("Command list:"
              "\naddTransaction - Adds an Entry into the checkbook",
              "\nhelp - Shows a list of commands",
              "\nrandomTransaction - creates a random entry to input into the ledger (for debug c:)",
              "\nlistTransactions - lists entries in ledger",
              "\nprintBalance - prints the current balance",
              "\nrecalculateBalance - Recalculates all balances",
              "\naddCategory - Add a category to choose from",
              "\nlistCategories - Lists all of the current categories to pick from"
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
        current_balance = getLastEntryAmount(file_path=file_path)
        print("Current Balance: ", round(float(current_balance), 2))

    elif command_input == "addCategory":
        user_input = str(input("Enter the categories name: "))
        saveCategory(user_input)
        print(user_input + " was added to the list of categories!")
    elif command_input == "listCategories":
        listCategory()
    else:
        print("That is not a valid command! Please try again.")
    return main()


def main():
    print() # Decorative Print
    active_ledger = "Checking"

    command_input = input("Please enter a command or type help: ")
    inputCommand(command_input, active_ledger=active_ledger)

    return


if __name__ == "__main__":  # Prevents being ran on an import
    main()
