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
    - create a def function to find if current day profit is lesser than previous day profit
    - subtract current day profit from previous day profit if previous day profit > current day profit
    """
    # create an empty list
    message = []
    # create 3 empty variables 
    counter = 0
    num = 0
    previous_profit = 0
    # use for loop to evaluate whether current day profit is greater than previous day profit 
    for i in netprofit: 
        #use float function to change net profit data in excel from string to number
        if float(i) > previous_profit:
            counter += 1
        else:
        # if profit data does not fulfill the if statement above (current day profit > previous day profit), profit deficit will be printed
        # use f string the store text, num and float(i) in same line
            print(f"[PROFIT DEFICIT] DAY:{Day[num]}, AMOUNT: USD{previous_profit - float(i)}")

        # use if counter == 6 to see if current day profit > previous day profit throughtout the 6 days
        # use return to print net profit surplus if conidtions for if statement is not met
        if counter == 6:
            message = "[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
         # f str containing day, previous_profit and i variable appended to message list
        else:
            message.append(f"[CASH DEFICIT] DAY:{Day[num]}, AMOUNT:USD{previous_profit - float(i)}")
        # previous_profit variable containing current i value
        previous_profit = float(i)
        # 1 is added to num variable and the value is referenced back to num variable
        num += 1

    # create a for loop
    for i in message:
        # write multiple lines using .writelines()
        file.writelines(i,"\n")

    # close summary_report.txt
    file.close()