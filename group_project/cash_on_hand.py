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
    - This function creates a path object for summary_report.txt and append data to file.
    - This function creates an empty variable for prev_coh, counter and num.
    - This function creates an empty list for message.
    - This function uses a global keyword to modify cashonhand and day variable outside the function.
    - This function adds 1 to the counter variable  if index of cashonhand is larger than prev_coh.
    - This function adds a string to the message list if counter is equivalent to number of days.
    - This function adds str containing day, prev_coh and i variable appended to message list when there is no cash surplus.
    - This function writes file.writelines(f"{i}") if iteration to find if length of i is greater than 1.
    - This function writes file.writelines(message) if iteration to find if length of i is not greater than 1.
    - This function closes summary_report.txt.
    """
    # create a path object for summary_report.txt
    fp = Path.cwd()/"group_project"/"summary_report.txt"
    # use mode = "a" to append data to file
    with fp.open(mode = "a", encoding= "UTF-8") as file:

        # create an empty variable for cash on hand for the previous day
        prev_coh = 0
        # create an empty list for message
        message = []
        # create an empty variable for counter
        counter = 0
        # create an empty variable for number
        num = 0
        
        # use a global keyword to modify cashonhand and day variable outside the function
        global cashonhand, day

        # for loop
        for i in cashonhand:

            # if iteration to find if index of cashonhand is larger than prev_coh
            if float(i) > prev_coh:
                # 1 is added to counter variable and the value is referenced back to counter variable
                counter += 1
                # if iteration to find if counter is equivalent to number of days, indicating all days have a cash surplus
                if counter == 6:
                    # str added to message list
                    message = ["[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"]
            # f str containing day, prev_coh and i variable appended to message list
            else:
                message.append(f"[CASH DEFICIT] DAY:{day[num]}, AMOUNT:USD{prev_coh - float(i)}")
            # prev_coh variable containing current i value
            prev_coh = float(i)
            # 1 is added to num variable and the value is referenced back to num variable
            num += 1
        # if iteration to find if length of i is greater than 1
        if len(message) > 1:
            # for loop
            for i in message:
                # write multiple lines using writelines()
                file.writelines(f"{i}")
        else:
            # write multiple lines using writelines
            file.writelines(message)
    # close summary_report.txt
    file.close()
