###################
# Checkbook Program
# Davin Young
# Florida Gulf Coast University
# Started Jan 2020
####################
from datetime import datetime, time, date
import json
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
                date_string = input(question)
                date_object = datetime.strptime(date_string, "%m/%d/%Y")
                break
            except ValueError:
                print("Incorrect format Use the format MM/DD/YYYY : ")
        return date_object

    ############################ Add entry to ledger ############################
    def addEntryToLedger(entryName, entryDate, entryAmount):
        newEntries = [entryName, str(entryDate), entryAmount]

        # with open('AccountingLedger.json', 'a') as json_file:
        #  json.dump(newEntries, json_file)

        f = open('AccountingLedger.json', 'r')
        data = json.load(f)
        f.close()
        for (k, v) in data.items():
            print("Key: " + k)
            print("Value: " + str(v))

        f = open('AccountingLedger.json', 'w')
        data = json.load(f)
        f.close()
        for (k, v) in data.items():
            print("Key: " + k)
            print("Value: " + str(v))

        #this crashes without a file set up. need to create a file with a basic json setup NOT EMPTY
        # PLAN THIS OUT ON PAPER

        '''
        ledger = []
        with open('AccountingLedger.json', 'r') as jsonFile:
            print(jsonFile)
            jsonObj = json.load(jsonFile)
            for entry in jsonObj['data']:
                ledgerFormatted = [entry[entryName], entry[entryDate], entry[entryAmount]]
                ledger.append(ledgerFormatted)
            #except missing file
                #create file
                #return to loading and adding entries
        '''

        print("Dumped", newEntries, " to the ledger.")
        return

    ############################ Create Entries ############################

    def createEntry():
        ### Asking for Input
        entryName = inputString("Please enter the entry's name: ")
        entryDate = inputDate("Please enter the entry's date \nUse the format MM/DD/YYYY : ")
        entryAmount = inputFloat("Please enter an amount : $")

        ## Save to data file
        addEntryToLedger(entryName, entryDate, entryAmount)

        return

    def createRandomEntry():
        randomNames = ["The Polar Fiddler", "The Olive Drum", "The Bengal Drum", "The Solar Castle", "The Fire Fusion",
                       "Cinnamon", "The Nightingale", "Fantasia", "Roadhouse"]
        entryName = random.choice(randomNames)

        start_date = date.today().replace(day=1, month=1).toordinal()
        end_date = date.today().toordinal()
        entryDate = date.fromordinal(random.randint(start_date, end_date))

        entryAmount = round((random.random() * 100 + random.random()), 2)

        addEntryToLedger(entryName, entryDate, entryAmount)
        return

    createRandomEntry()  ######## <<--------------------- c: -------------------------------- REMOVE ME --------------

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


############################ Book Entry Class ############################
class BookEntry(object):

    def __init__(self, name, date, amount):
        self.name = name
        self.date = date
        self.amount = amount


if __name__ == "__main__":
    main()
