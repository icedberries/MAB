from pathlib import Path

import csv

file_path = Path.cwd()/"group_project/csv_reports/Profit and Loss.csv"

with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    Day = []
    netprofit = []

    for row in reader:
        Day.append(row[0])
        netprofit.append(row[4])

def profit():

    counter = 0
    num = 0
    previous_profit = 0

    for i in netprofit:
        if float(i) > previous_profit:
            counter += 1
        else:
            print(f"[PROFIT DEFICIT] DAY:{Day[num]}, AMOUNT: USD{previous_profit - float(i)}")

        previous_profit = float(i)
        num += 1

        if counter == 6:
            return "[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
        