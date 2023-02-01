from pathlib import Path

import csv

file_path = Path.cwd()/"C:\Profit and Loss\profit_and_loss.csv"

with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    
    previous_profit = 0

    Day = []
    netprofit = []

    for row in reader:
        Day.append(row[0])
        netprofit.append(row[4])

    print(Day)
    print(netprofit)

def profit(Day,netprofit,previous_profit):

    counter = 0
    num = 0

    for i in netprofit:
        if float(i) > previous_profit:
            counter += 1
        else:
            print(f"[CASH DEFICIT] DAY:{Day[num]}, AMOUNT: USD{float(i) - previous_profit}")

        previous_profit = float(i)
        num += 1

        if counter == 6:
            return "[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"

print(profit(Day,netprofit,previous_profit))
