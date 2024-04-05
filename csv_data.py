import csv

import si

filename = 'sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs = [], []
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    for row in reader:
        highs.append(row[5])
    print(highs)

#Also followed directions and commands from Python Crash Course 2nd Edition

