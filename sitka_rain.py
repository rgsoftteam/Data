import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	# чтение осадков из файла
	dates, rains = [], []
	for row in reader:
		current_date = datetime.strptime(row[2], "%Y-%m-%d")
		rain = float(row[3])
		dates.append(current_date)
		rains.append(rain)
	
	# нанесение данных на диаграмму
	plt.style.use('seaborn')
	fig, ax = plt.subplots()
	ax.plot(dates, rains, c='blue', alpha=0.5)
	
	# форматирование диаграммы
	plt.title("Daily rains Sitka-2018", fontsize=24)
	plt.xlabel('', fontsize=16)
	fig.autofmt_xdate()
	plt.tick_params(axis='both', which='major', labelsize=16)

	plt.show()