from pathlib import Path
import csv

fp = Path.cwd()/"group_project"/"csv_reports"/"Cash on Hand.csv"

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    prev_coh = 0

    day = []
    cashonhand = []

    for row in reader:
        day.append(row[0])
        cashonhand.append(row[1])

def value():
    """
    - This function
    """

    counter = 0
    num = 0

    global cashonhand, prev_coh, day

    for i in cashonhand:
        if float(i) > prev_coh:
            counter += 1
        else:
            return f"[CASH DEFICIT] DAY:{day[num-1]}, AMOUNT:USD{i - prev_coh}"
        prev_coh = float(i)
        num += 1

    if counter == 6:
        return "[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
