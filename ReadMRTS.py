import csv

# Reading from MRTS cleaned csv file
with open('mrts.csv') as file:
    #read csv file
    csv_file = csv.reader(file, delimiter=',')
    #loop through the data
    for row in csv_file:
          print(row)

          