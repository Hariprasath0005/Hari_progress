from prettytable import PrettyTable
table = PrettyTable()

table.add_column("names",["Hari","Ganesh"])
table.add_column("last name",["T","T"])
table.align="r"
print(table)