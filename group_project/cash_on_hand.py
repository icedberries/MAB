from pathlib import Path
import csv

#create a file to csv file
fp = Path.cwd()/"group_project"/"csv_reports"/"Cash on Hand.csv"

#read the csv file to append day and cash on hand from the csv
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)

#create an empty variable for the cash on hand for the previous day
    prev_coh = 0

    day = []

    cashonhand = []


    for row in reader:           
        day.append(row[0])
        cashonhand.append(row[1])

    print(day)
    print(cashonhand)

def value(day, cashonhand, prev_coh):
    """
    - This function
    """

    counter = 0
    num = 0

    for i in cashonhand:
        if float(i) > prev_coh:
            counter += 1
        else:
            return f"[CASH DEFICIT] DAY:{day[num-1]}, AMOUNT:USD{i - prev_coh}" 
        prev_coh = float(i)
        num += 1

    if counter == 6:
        return "[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"

print(value(day, cashonhand, prev_coh))
