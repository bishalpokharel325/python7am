import csv
def csvtolistconverter(filename):
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data
