from pathlib import Path
import csv

# use .cwd() function to import Profit and Loss csv file 
file_path = Path.cwd()/"group_project/csv_reports/Profit and Loss.csv"

# read the csv file to append profit and quantity from the csv.
with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)

#create 2 empty lists
    Day = []
    netprofit = []

# use for loop to append day number in row 0 and profit in row 4
    for row in reader:
        Day.append(row[0])
        netprofit.append(row[4])

def profit():
    """
    - use def function to subtract current day profit from previous day profit if current day profit < previous day profit
    """
    counter = 0
    num = 0
    previous_profit = 0

    # use for loop 
    # use if and else to compare profit of current day and previous day
    # if profit of previous day is more than current day, a statement showing the day of 
    for i in netprofit:
        if float(i) > previous_profit:
            counter += 1
        else:
            print(f"[PROFIT DEFICIT] DAY:{Day[num]}, AMOUNT: USD{previous_profit - float(i)}")

        previous_profit = float(i)
        num += 1

        # use if function to print out net profit surplus if all profits in current day is higher than previous day
        if counter == 6:
            return "[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
