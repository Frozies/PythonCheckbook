# PythonCheckbook
Welcome to my accounting Program. This project was created as a final for COP1500.

Apon running this program, it will create a new folder, "/data", in the root directory of the file. A ledger file, "Checking.csv", and a categories file, "Categories.config". Both of these files can be edited in any excel editor and a text editor.

The ledger file has five columns; Entry Name, Entry Amount, Entry Date, Category, and Current Balance. Each entry will be added to a new line regardless of the entry date.

The category file can be edited or added to either in program or in a text editor. The default categories are: No Category, Income, Groceries, Housing, Transportation, Food, Utilities, Insurance, Medical, Savings, Entertainment/

# Commands:
All these are case sensative

addTransaction - This promts the user for information about the transaction intended to be entered into the ledger.
help - Lists all the commands in the program.
randomTransaction - Randomly generates a tranaction to be entered into the ledger.
listTransactions - Shows a list of all the entries in the ledger file.
balance - Shows your current balance after the last entry.
addCategory - Adds to the category config file.
categories - Lists all of the categories currently in the associated config file.
spending - Adds up all of the transaction with their respected categories and shows the totals.
