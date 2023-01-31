from pathlib import Path
import csv

file_path = Path.cwd()/"csv_reports"/"Overheads.csv"

with file_path.open(mode='r', encoding='UTF-8') as file:
    reader = csv.reader(file)
    next(reader)
    cat = []
    num = []
    for row in reader:
        cat.append(row[0])
        num.append(float(row[1]))
    diction = {}
    for each_value in num:
        for each_cat in cat:
            diction[each_value] = each_cat
            value = max(diction)
    print(f"[HIGHEST OVERHEADS] {diction[value].upper()}: {value}")