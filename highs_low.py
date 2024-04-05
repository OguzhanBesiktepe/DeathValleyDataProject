filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
 reader = csv.reader(f)
 header_row = next(reader)

 # Get dates, and high and low temperatures from this file.
 dates, highs, lows = [], [], []
 for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[5])
    low = int(row[6])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')

# Format plot.
plt.title("Daily high and low temperatures - 2018", fontsize=24)