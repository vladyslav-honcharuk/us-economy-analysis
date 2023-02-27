import csv

# Reading from drinks sample csv file
with open('sample_drinks.csv') as file:
    #read csv file
    csv_file = csv.reader(file, delimiter=',')
    #loop through the data
    for row in csv_file:
          print(row)

          