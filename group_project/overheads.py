#import Path method from pathlib
from pathlib import Path
# Import csv module
import csv

# specification of file path for reading
file_path = Path.cwd()/"csv_reports"/"Overheads.csv"

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

    for row in reader:
        cat.append(row[0])
        num.append(float(row[1]))

def overhead():
    """
    - The function
    """
    # create an empty dictionary
    diction = {}
    
    # merging of two lists into a dictionary by for loop
    for each_value in num:
        for each_cat in cat:
            diction[each_value] = each_cat
            # assign a variable when finding the maximum value 
            value = max(diction)
    return f"[HIGHEST OVERHEADS] {diction[value].upper()}: {value}"
   