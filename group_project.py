from pathlib import Path
import csv

file_path = Path.cwd()/"overheads-day-90.csv"


with file_path.open(mode='r', encoding='UTF-8') as file:
    reader = csv.reader(file)
    next(reader)
    cat = []
    num = []
    highest_num = []
    for row in reader: 
        cat.append(row[0])
        num.append(float(row[1]))
        highest_num.append(max(num))
    diction = {}
    for each_cat in cat:
        for each_value in num:
            diction[each_cat] = each_value
            num.remove(each_value)
            break
    print(diction['Salary Expense'])
    

    #for row in reader:
        #numbers = (row[1])
        #num.append(float(numbers))
    #print(max(num))
        #everything.append(row[0])
        #num.append(float(row[1]))
        #diction = {} 
        #for each in cat:
        #    print(each)
        #    for every in num:
        #        diction[each] = every
        #        num.remove(every)
        #        break
        #    print(diction)

    #print(everything)
    #print(cat)
    #print(num)

    
        
    