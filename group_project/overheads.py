from pathlib import Path
import csv

file_path = Path.cwd()/"group_project"/"csv_reports"/"Overheads.csv"

with file_path.open(mode='r', encoding='UTF-8') as file:
    reader = csv.reader(file)
    # skip the header
    next(reader)
    # create empty lists to store the categories and values

cat = []

num = []

def overhead():
    """
    - The function
    """
    for row in reader:
        cat.append(row[0])
        num.append(float(row[1]))
    # create an empty dictionary 
    diction = {}
    for each_value in num:
        for each_cat in cat:
            diction[each_value] = each_cat
            value = max(diction)
    return f"[HIGHEST OVERHEADS] {diction[value].upper()}: {value}"

print(overhead())