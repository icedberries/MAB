from pathlib import Path
import csv

#create a file to csv file
fp = Path.cwd()/"group_project"/"csv_reports"/"Cash on Hand.csv"

#read the csv file to append day and cash on hand from the csv
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)

#create an empty variable for cash on hand for the previous day
    prev_coh = 0

#create an empty list to store the days
    day = []

#create an empty list to store the cash on hand
    cashonhand = []

#append day and cash on hand as a list back to each empty list using the for loop
    for row in reader:           
        day.append(row[0])
        cashonhand.append(row[1])

#define value()
def value():
    """
    - This function
    """
    # create a path object for summary_report.txt
    fp = Path.cwd()/"group_project"/"summary_report.txt"
    # use mode = "a" to append data to file
    with fp.open(mode = "a", encoding= "UTF-8") as file:

        #create an empty variable for cash on hand for the previous day
        prev_coh = 0
        #create an empty list for message
        message = []
        #create an empty variable for counter
        counter = 0
        #create an empty variable for number
        num = 0
        
        #use a global keyword to modify cashonhand and day variable outside the function
        global cashonhand, day

        #for loop
        for i in cashonhand:

            #if iteration to find if index of cashonhand is larger than prev_coh
            if float(i) > prev_coh:
                #1 is added to counter variable and the value is referenced back to counter variable
                counter += 1
                #if iteration to find if counter is equivalent to number of days, indicating all days have a cash surplus
                if counter == 6:
                    message = ["[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"]
            else:
                message.append(f"[CASH DEFICIT] DAY:{day[num]}, AMOUNT:USD{prev_coh - float(i)}")
            prev_coh = float(i)
            num += 1

        if len(message) > 1:
            for i in message:
                file.writelines(f"{i}")
        else:
            file.writelines(message)
    # close summary_report.txt
    file.close()
