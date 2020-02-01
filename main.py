###################
# Checkbook Program
# By Davin Young
####################


def main():
    fileIO


def inputInteger(question):  # N for Number
    while True:
        try:
            n = int(input(question))
            break
        except ValueError:
            print("No valid integer! Please try again ...")
    print("Great, you successfully entered an integer!")
    return main()


""" # Unnecessary code. Strings don't really break most of the time.
def inputString(question):
    while True:
        try:
            s = str(input(question))
            break
        except ValueError:
            print("No valid string! Please try again ...")
    print("Great, you successfully entered a string!")
    return main()
"""

if __name__ == "__main__":
    main()
