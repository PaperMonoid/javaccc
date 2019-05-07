import csv

input_file = "example.csv"

with open(input_file) as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    for [name, rule] in reader:
        print("void {0}():\n{{ }}\n{{\n\t{1}\n\t{{\n\t\t// TODO: implement AST\n\t}}\n}}".format(name, rule))
        print("")
