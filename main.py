###################
# Checkbook Program
# By Davin Young
####################
from datetime import datetime

from pip._vendor.distlib.compat import raw_input


def main():
    ############################ User Input Methods ############################
    def inputInteger(question):  # N for Number
        while True:
            try:
                n = int(input(question))
                break
            except ValueError:
                print("No valid integer! Please try again ...")
        return n

    def inputString(question):
        while True:
            try:
                s = str(input(question))
                break
            except ValueError:
                print("No valid string! Please try again ...")
        return s

    def inputDate(question):
        while True:
            try:
                date_string = input(question)
                date_object = datetime.strptime(date_string, "%m/%d/%Y")
                break
            except ValueError:
                print("Incorrect format Use the format DD/MM/YYYY : ")
        return date_string

    ############################ Book Entry ############################
    def bookEntry():
        entryName = inputString("Please enter the entry's name: ")
        entryDate = inputDate("Please enter the entry's date \nUse the format DD/MM/YYYY : ")

        return entryName, entryDate

    print("You entered:", bookEntry())


if __name__ == "__main__":
    main()
