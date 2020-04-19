"""Accounting Ledger"""
__author__ = "Davin Young"

import csv
import math
import os
import random
from datetime import datetime, date


def getLastEntryAmount(file_path):
    """
    Reverses the ledger to get the most recent entry at the very bottom of the
    list. Returns a specific value by row and column.

    Parameters:
        file_path (str): The location of the current ledger.

    Returns:
        retrieved_data (str): The value under the column and row selected.
                             Currently set to the value of last set balance.
    """

    checkLedgerPath(file_path=file_path)

    file_name = loadCSV(input_file_name='Checking', print_values=False)

    with open(file_name) as file:
        # Opens file

        reader = csv.reader(file)
        # Reads file with dict reader

        data = [row for row in reader]
        # Sets the list data to a variable

        data_reversed = data[::-1]
        # Slice - No value before or after the first colon and increment by -1

        row_index = 4
        # Pick what row you want

        column_data = [row[row_index] for row in data_reversed]
        # Chooses a column based on the number you pick

        retrieved_data = column_data[0]
        # Picks the first values

    return retrieved_data


def inputInteger(question):
    """
    Allows Integer input that throws an error for exceptions

    Parameters:
        question (str): Function input to ask for user's input.

    Returns:
        input_number (int): User's input in response to the question given.
    """

    while True:

        try:
            input_number = int(input(question))
            break

        except ValueError:
            print("No valid integer! Please try again ...")

    return input_number


def inputFloat(question):
    """
    Allows Float input that throws an error for exceptions

    Parameters:
        question (str): Function input for a question for user input.

    Returns:
        input_number (float): User's input in response to the question given.
    """
    while True:

        try:
            input_number = float(input(question))
            break

        except ValueError:
            print("No valid Float! Please try again ...")

    return input_number


def inputString(question):
    """
    Allows string input that throws an error for exceptions

    Parameters:
        question (str): Function input of a question to ask for user input.

    Returns:
        input_string (str): User input response from question given.
    """
    while True:

        try:
            input_string = str(input(question))
            break

        except ValueError:
            print("No valid string! Please try again ...")

    return input_string


def inputDate(question):
    """
    Allows date input that throws an error for exceptions

    Parameters:
        question (str): Function input of what question to ask for the user
                        input.

    Returns:
        date_object (date_object): A date in the form of mm/dd/yyyy
    """
    while True:
        try:
            date_string = input(question)
            if date_string == "":
                date_object = date.today().strftime('%m/%d/%Y')
                # Uses date class to get today's date in mm/dd/yyyy format
            else:
                date_object = datetime.strptime(date_string,
                                                "%m/%d/%Y").strftime(
                    '%m/%d/%Y')
                # Checks formatting
            break

        except ValueError:
            # Checks if the format is not correct
            print("Incorrect format Use the format MM/DD/YYYY : ")

    return date_object


def checkLedgerPath(file_path):
    """
     Looks for the indicated file. If the file is not found, try creating it.
     If there is no data written to the file, save the indicated field_names as
     a header.

    Parameter:
        file_path (str) : The string of the location of the ledger to check
    """

    directory = os.path.dirname(file_path)

    ledger_size = 0

    field_names = ['Entry Name', 'Entry Amount', 'Entry Date', 'Category',
                   'Current Balance']
    # Sets up variable names for csv header

    if not os.path.exists(directory):  # If it doesn't exists, create one.
        try:
            os.makedirs(directory)
            # Creates the folder but will not fill it with anything
        except PermissionError:
            print("It seems like you cant write to this file. Please try"
                  " again.")
            main()

    try:
        ledger_size = os.stat(file_path).st_size
        # Try to set the ledger's file size to that of the indicated ledger

    except FileNotFoundError:
        print("Ledger file not found. Creating one now!")

        open(file_path, 'x')
        # Creates the file without writing any data.

    if ledger_size == 0:
        writeDataToCSV(file_path=file_path, entry_data=field_names)

    return


def loadCSV(input_file_name, print_values, list_amount=0):
    """
    After checking for it's existence, load the csv file into memory and
    if printValues is true, read through and print the an equivalent number to
    list amount. Checks against a few cases like if list_amount is > 0, == 0,
    and < 0, as well as if there are no entries.

    Parameters:
        input_file_name (str): The ledger file name to load into memory
        print_values (bool): Whether or not to print the values loaded to logs
        list_amount (int): How many entries to list to screen when printed.
    
    Returns:
        file_path (str):

    """

    directory = os.path.abspath(os.path.join(
        os.path.curdir))
    # Initializes directory to the current directory

    file_path = directory + "/data/" + input_file_name + ".csv"
    # Sets directory item /data/filename.csv to variable

    checkLedgerPath(file_path)
    # Checks if the variable file_name is a valid path

    if os.path.exists(file_path) & print_values is True:
        # Checks if there is a file, and if print values is true

        with open(file_path) as file:
            # Opens file

            reader = csv.reader(file)
            # Reads file with dict reader

            index = 0

            if list_amount == 0 or list_amount < 0:
                for row in reader:
                    if index == 0:

                        print('{:<25} {:<15} {:<15} {:<15} {:<15}'.format(
                            *row))
                        # Prints Header without '$'

                    else:
                        print('{:<25} ${:<15} {:<15} {:<15} ${:<15}'.format(
                            *row))
                        # Prints a '$' on any transactions

                    index += 1

            elif list_amount > 0:

                data = [row for row in reader]
                # Sets the list data to a variable

                data_reversed = data[::-1]

                if not len(data_reversed) - 1 <= list_amount:
                    while index < list_amount - 1:
                        for row in data_reversed:
                            if index <= list_amount - 1:
                                print(
                                    '{:<25} ${:<15} {:<15} {:<15} ${:<15}'
                                        .format(*row))

                                index += 1

                else:
                    for row in data_reversed:
                        if index < len(data_reversed) - 1:
                            print(
                                '{:<25} ${:<15} {:<15} {:<15} ${:<15}'.format(
                                    *row))

                            index += 1
    return file_path


def saveCSV(ledger_name, entry_data):
    """
    Saves all of the data from entry_data to the specified ledger file after
    checking for it's existence. Calculates out the current balance from adding
    the current entry with the previous amount's. If one does not exist,
    feed the current entry's value.

    Parameters:
        ledger_name (str): The ledger file's name to be saved to.
        entry_data (list): A list of entry data from addEntryToLedger in the
                          form [entry_name, entry_amount, entry_date,
                          category_index]
    """
    directory = os.path.abspath(os.path.join(os.path.curdir))
    # Initializes directory to the current directory.

    file_path = directory + "/data/" + ledger_name + ".csv"
    # Sets directory item /data/filename.csv to variable.

    checkLedgerPath(file_path)
    # Checks if the variable file_path is a valid path.

    entry_amount = entry_data[1]

    if not getLastEntryAmount(file_path=file_path) == "Current Balance":

        current_balance = round(float(entry_amount) + float(
            getLastEntryAmount(file_path=file_path)), 2)

    else:
        current_balance = float(entry_amount)

    entry_data.append(float(current_balance))

    writeDataToCSV(file_path=file_path, entry_data=entry_data)

    return


def writeDataToCSV(file_path, entry_data):
    """
    Iterate through each record in the input entry_data and saves the data to
    the opened csv file from file_path.

    Parameters:
        file_path(str): A direct path string to the ledger
        entry_data(list): Retrieves a list from the previous function to save
                         to save to a csv file
    """

    count = 0

    # This fills in data like a type writer

    for record in entry_data:

        if count == len(
                entry_data) - 1:
            # Checks to see if the current record section is the last.

            csv_file = open(file_path, 'a')

            csv_file.write('%s\n' % record)
            # Prints a new line with no comma

        if count != len(
                entry_data) - 1:
            # If not the last record, then write the key value with a comma
            try:
                csv_file = open(file_path, 'a')
            except PermissionError:
                print("It seems like you cant write to this file. Please try"
                      " again.")
                main()

            csv_file.write('%s,' % record)

            count += 1  # Increase record count

        csv_file.close()

    return


def addEntryToLedger(entry_name, entry_date, entry_amount, category_index):
    """
    Combines all the input parameters into a list and sends it off to be saved.
    Prints the saved data
Parameters:
        entry_name (str): User input of a string to add to a ledger entry
        entry_date (datetime): User input of a date mm/dd/yyyy
        entry_amount (float): User input of a float to add to ledger entry
        category_index (int): User input index from a list of category.config

    TODO: Combine this directly into saveCSV
    """

    entry_data = [entry_name, entry_amount, entry_date,
                  category_index]
    # Sets up variables for ledger data based off of input

    saveCSV("Checking", entry_data)
    # appends the entry data to the csv file

    print(entry_name, "totaling $" + str(entry_amount), "on", entry_date,
          "under the category", category_index,
          "was added to the ledger!")

    return


def createEntry():
    """
    Asks the user for a variety of inputs to send to the addEntryToLedger
    function.

    User input of an entry_name, entry_date, entry_amount, and category_index.
    """
    # Asking for Input
    entry_name = inputString("Please enter the entry's name: ")

    entry_date = inputDate(
        "Please enter the entry's  or leave blank to use today's date" +
        "\nUse the format MM/DD/YYYY : ")

    entry_amount = inputFloat(
        "Please enter an amount, use a negative for any bills: $")

    listCategory()

    category_index = inputInteger(
        "\nPlease select a category by typing it's number: ")

    directory = os.path.abspath(os.path.join(
        os.path.curdir))
    # Initializes directory to the current directory

    file_path = directory + "/data/Categories.config"
    # Sets directory item /data/filename.csv to variable

    cat_list = [line.rstrip('\n') for line in open(file_path)]

    ## Save to data file
    addEntryToLedger(entry_name, entry_date, entry_amount,
                     cat_list[category_index])

    return


def createRandomEntry():
    """
    Using the preset functions for creating an entry, choose random values
    to input into a new transaction.

    Chooses from a list of names randomly.
    Picks a random date in range of Jan 1st to the local date.
    Generates a random number from 0.00 to 100.99 as the entry amount.
    Randomly decides whether to negate it.
    Finally chooses a random category from the categories.config file and
    sends this data to the addEntryToLedger function.
    """

    random_names = ["The Polar Fiddler", "The Olive Drum", "The Bengal Drum",
                    "The Solar Castle", "The Fire Fusion",
                    "Cinnamon", "The Nightingale", "Fantasia", "Roadhouse"]

    entry_name = random.choice(
        random_names)
    # Chooses a random name from the list above

    start_date = date.today().replace(day=1, month=1).toordinal()
    # Sets Jan 1st as start date

    end_date = date.today().toordinal()
    # Picks sets today as the end date

    random_date = date.fromordinal(random.randint(start_date, end_date))
    # Picks a random date in between

    entry_date = datetime.strptime(str(random_date), '%Y-%m-%d').strftime(
        '%m/%d/%Y')
    # Formats the date correctly

    entry_amount = round((random.random() * 100 + random.random()), 2)
    # Picks a random amount with decimal

    if bool(random.getrandbits(1)):
        # Randomizes to count as bill or income

        entry_amount = entry_amount * -1
        # Negates the number.

    checkCategoryPath()

    directory = os.path.abspath(os.path.join(
        os.path.curdir))
    # Initializes directory to the current directory

    file_path = directory + "/data/Categories.config"
    # Sets directory item /data/filename.csv to variable

    cat_list = [line.rstrip('\n') for line in open(file_path)]

    random_category_index = round(random.random() * len(cat_list) - 1)
    # Choose a random category.

    addEntryToLedger(entry_name, entry_date, entry_amount,
                     cat_list[random_category_index])
    # Adds entry to ledger

    return


def saveCategory(entry_data):
    """
    Using the user input as entry_data, this function writes the string to a new
    line in the file under "/../data/Categories.config"

    Parameters:
        entry_data (str): The user input string for a new category.

    """

    directory = os.path.abspath(os.path.join(
        os.path.curdir))  # initializes directory to the current directory

    file_path = directory + "/data/Categories.config"
    # sets directory item /data/filename.csv to variable

    checkCategoryPath()
    try:
        with open(file_path, 'a') as file:
            file.write(str(entry_data) + "\n")
    except PermissionError:
        print("It seems like you cant write to this file. Please try"
              " again.")
        main()

    return


def checkCategoryPath():
    """
    Opens the path to the categories.config file and checks for it's existence.
    Try to check for a file size and throws an error for a missing file, which
    then creates it. If there is no data in the config, The function fills it.
    """

    directory = os.path.abspath(os.path.join(
        os.path.curdir))
    # Initializes directory to the current directory

    file_path = directory + "/data/Categories.config"
    # Sets directory item /data/filename.csv to variable

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

    if not os.path.exists(directory):  # If it doesn't exists, create one.
        try:
            os.makedirs(directory)
            # Creates the folder but will not fill it with anything
        except PermissionError:
            print("It seems like you cant write to this file. Please try"
                  " again.")
            main()

    try:
        ledger_size = os.stat(file_path).st_size
        # Sets the var ledger_size to see if its a new file or not.

    except FileNotFoundError:
        print("Categories configuration file now found. Creating one now!")
        try:
            os.mkdir(directory + "/data/")

        except FileExistsError:
            print("Data folder already exists!")
            pass

        open(file_path, 'x')

    if ledger_size == 0:
        with open(file_path, 'a') as file:
            file.write(default_categories)

    return


def listCategory():
    """
    After checking for it's existence, the categories.config is opened and
    printed out in 3 entries per row.
    """
    checkCategoryPath()

    directory = os.path.abspath(os.path.join(os.path.curdir))
    # Initializes directory to the current directory

    filePath = directory + "/data/Categories.config"
    # Sets directory item /data/filename.csv to variable

    count = 0

    catList = [line.rstrip('\n') for line in open(filePath)]

    for x in range(math.ceil(len(catList) / 3)):
        # Ceiling(categories index / 3)

        for y in range(3):

            if count <= (len(catList) - 1):
                print(str(count) + ".) " + str(catList[count]) + " ", end=" ")
                count += 1

        print()

    return


def sumCategories(active_ledger):
    """
    Opens the defined active_ledger, reverses the data, selects both the
    category row and the coinciding value row. Then creates a dictionary from
    each of the categories. Finally iterates through each entry and adds it
    to its proper index in the dictionary.

    Parameters:
        active_ledger (str): This is the file path location of a ledger csv.
    """

    ledger_path = loadCSV(input_file_name=active_ledger, print_values=False)

    with open(ledger_path) as file:  # Opens file

        reader = csv.reader(file)  # Reads file with dict reader
        data = [row for row in reader]  # Sets the list data to a variable

        data_reversed = data[
                        ::-1]
        # Slice - No value before or after the first colon and increment by -1

        value_index = 1
        category_index = 3

        category_data = [row[category_index] for row in
                         data_reversed]
        # Chooses a column based on the number you pick

        value_data = [row[value_index] for row in
                      data_reversed]
        # Chooses a column based on the number you pick

        category_value = dict()

        for i in range(0, len(data_reversed) - 1):
            current_category = category_data[i]
            current_value = value_data[i]

            sum_values = float(current_value) + float(
                category_value.get(current_category, 0))

            category_value[current_category] = round(sum_values, 2)

        print("Overall Budget\n")

        print(f"\n".join("{:<15}\t${}".format(key, value) for key, value in
                         category_value.items()))

    return


def inputCommand(command_input, active_ledger):
    """
    Retrieves the user's input to check against a list of strings with
    booleans. Then returns to main.

    easy to expand!
    if commandInput == "foo":
        bar()
    elif commandInput == "bar":
        baz()

    Parameters:
        command_input (str): This is the user input from main.
        active_ledger (str): This is the file path location of a ledger csv.

    Returns:
        main() : Jumps back to the main function to repeat the loop.
    """

    print()  # Decorative Print

    directory = os.path.abspath(os.path.join(os.path.curdir))
    # initializes directory to the current directory

    file_path = directory + "/data/" + active_ledger + ".csv"
    # sets directory item /data/filename.csv to variable

    if command_input == "help":
        print("Command list:"
              "\naddTransaction - Adds an Entry into the checkbook",

              "\nhelp - Shows a list of commands",

              "\nrandomTransaction - creates a random entry to input "
              "into the ledger (for debug c:)",

              "\nlistTransactions - lists entries in ledger",

              "\nbalance - prints the current balance",

              "\naddCategory - Add a category to choose from",

              "\ncategories - Lists all of the current categories to "
              "pick from",

              "\nspending - List all of the spending organized by category")

    elif command_input == "addTransaction":
        createEntry()

    elif command_input == "randomTransaction":
        createRandomEntry()

    elif command_input == "listTransactions":
        loadCSV("Checking", print_values=True)

    elif command_input == "balance":
        current_balance = getLastEntryAmount(file_path=file_path)
        print("Current Balance: ", round(float(current_balance), 2))

    elif command_input == "addCategory":
        user_input = str(input("Enter the categories name: "))
        saveCategory(user_input)
        print(user_input + " was added to the list of categories!")

    elif command_input == "categories":
        listCategory()

    elif command_input == "spending":
        sumCategories(active_ledger=active_ledger)

    else:
        print("That is not a valid command! Please try again.")

    return main()


def main():
    """
    The main function loops through two separate functions; asking for the user
    input and sending that input to the inputCommand function for parsing.
    """
    print()  # Decorative Print
    active_ledger = "Checking"

    command_input = input("Please enter a command or type help: ")
    inputCommand(command_input, active_ledger=active_ledger)

    return


def startup():
    """
    This is the startup function. It chooses the save location of the checking
    ledger CSV File and checks and prints the balance. Then lists
    the most recent few transactions. It finally jumps to the main function.
    """

    directory = os.path.abspath(os.path.join(os.path.curdir))
    # initializes directory to the current directory

    checking_file_path = directory + "/data/" + "Checking.csv"

    checking_balance = getLastEntryAmount(file_path=checking_file_path)

    # savings_file_path = directory + "/data/" + "savings.csv"
    # savings_balance = getLastEntryAmount(file_path=savings_file_path)

    print("Welcome to my accounting software!")

    try:
        if float(checking_balance):
            # Check if there is a number to print

            print("Current Balance in checking: $" + str(
                round(float(checking_balance), 2)))

        else:
            print("Current Balance in checking: ", "$0.00")

    except ValueError:  # Default to 0.00
        print("Current Balance in checking: ", "$0.00")

    # print("Current Balance in savings: ", round(float(savings_balance), 2))

    print("\nHere are the last few transactions")

    fieldNames = "{:<25} {:<15} {:<15} {:<15} {:<15}"
    # Formatting

    print(fieldNames.format("Entry Name", "Entry Amount", "Entry Date",
                            "Category", "Current Balance"))

    loadCSV(input_file_name="Checking", print_values=True, list_amount=5)

    main()


if __name__ == "__main__":
    startup()  # Runs the program
