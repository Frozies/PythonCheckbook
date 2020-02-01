###################
# Checkbook Program
# Davin Young
# Florida Gulf Coast University
# Started Jan 2020
####################
from datetime import datetime


def main():

    ############################ User Input Methods ############################

    def inputInteger(question): ##### Allows Integer input that throws an error for exceptions
        while True:
            try:
                n = int(input(question))
                break
            except ValueError:
                print("No valid integer! Please try again ...")
        return n

    def inputFloat(question): ##### Allows Float input that throws an error for exceptions
        while True:
            try:
                f = float(input(question))
                break
            except ValueError:
                print("No valid Float! Please try again ...")
        return f

    def inputString(question): ##### Allows string input that throws an error for exceptions
        while True:
            try:
                s = str(input(question))
                break
            except ValueError:
                print("No valid string! Please try again ...")
        return s

    def inputDate(question): ##### Allows date input that throws an error for exceptions
        while True:
            try:
                date_string = input(question)
                date_object = datetime.strptime(date_string, "%m/%d/%Y")
                break
            except ValueError:
                print("Incorrect format Use the format MM/DD/YYYY : ")
        return date_string

    ############################ Book Entry ############################
    def bookEntry():
        entryName = inputString("Please enter the entry's name: ")
        entryDate = inputDate("Please enter the entry's date \nUse the format MM/DD/YYYY : ")
        entryAmount = inputFloat("Please enter an amount : $")

        return entryName, entryDate, format(entryAmount, ",.2f")
        ### Reformat the value to have a comma every 3 places, and 2 decimal points

    ############################ RUN ############################
    print("You entered:", bookEntry())


if __name__ == "__main__":
    main()
