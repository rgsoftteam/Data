import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'data/death_valley_2018_simple.csv'

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	# чтение дат, максимальных и минимальных температур из файла
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
	title = "Daily rains - 2018\nDeath Valley, CA"
	plt.title(title, fontsize=20)
	plt.xlabel('', fontsize=16)
	fig.autofmt_xdate()
	plt.ylabel("Water (mm)", fontsize=16)
	plt.tick_params(axis='both', which='major', labelsize=16)

	plt.show()