#import Path method from pathlib
from pathlib import Path
# Import csv module
import csv

# specification of file path for reading
file_path = Path.cwd()/"group_project"/"csv_reports"/"Overheads.csv"

with file_path.open(mode='r', encoding='UTF-8') as file:
    # instantiate a read object
    reader = csv.reader(file)
    # skip the header
    next(reader)
    # create empty lists to store the categories and values
    cat = []
    num = []

    #for loop
    for row in reader:
        # use .append to append a new element in the empty list
        # row[0] stands for the expense category, which is at index 0
        cat.append(row[0])
        # row[1] stands for the values which is at index 1
        # use float() to convert strings to float to find maximum 
        num.append(float(row[1]))

# creation of function 
def overhead():
    """
    - The function merges the two lists created from above into a dictionary
    - The function then finds the maximum value and its relevant cateogory
    """
    fp = Path.cwd()/"group_project"/"summary_report.txt"
    # use mode = "a" to append data to file
    with fp.open(mode = "w", encoding= "UTF-8") as file:    
        
        # create an empty dictionary
        diction = {}

        # merging of two lists into a dictionary by for loop
        for each_value in num:
            for each_cat in cat:
                # assigning each value to their respective categories
                diction[each_value] = each_cat
                # assign a variable when finding the maximum value 
                value = max(diction)
        # create a variable to store f strings
        message = f"[HIGHEST OVERHEADS] {diction[value].upper()}: {value}%"
        file.write(f"{message}\n")
    file.close()
