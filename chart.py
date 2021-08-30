import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pickle
import matplotlib.dates as mdates
from datetime import datetime


with open('btc_price_history.txt', 'rb') as fp:
    data = pickle.load(fp)


class extract_price_and_date:
    def __init__(self, data):
        self.data = np.array(data, dtype=object)

    def price_and_date(self):
        price = []
        dates = []
        market_cap = []
        for i in range(0, len(self.data)-1):
            price.append(self.data[i][0]['price'])
            dates.append(self.data[i][0]['timestamp'])
            market_cap.append(self.data[i][0]['market_cap'])
        return price, dates, market_cap


p, d, m_cap = extract_price_and_date(data).price_and_date()
date = list(map(str, [string[:10] for string in d]))


a = [datetime.strptime(dat, '%Y-%m-%d') for dat in date]
x = matplotlib.dates.date2num(a)

formatter = matplotlib.dates.DateFormatter('%Y\n%b\n')

label_interval = mdates.YearLocator(2)
sub_label_interval = mdates.MonthLocator(interval=1)

plt.style.use('dark_background')
plt.gca().xaxis.set_major_formatter(formatter)
plt.gca().xaxis.set_major_locator(label_interval)
plt.gca().xaxis.set_minor_locator(sub_label_interval)
plt.gca().format_ydata = lambda x1: f'${x1:.2f}'
plt.grid(True)
plt.yscale('log')
plt.title('BTC Risk Index')
plt.ylabel('Price (USD)')
plt.xlabel('Dates')

plt.margins(0.1)
plt.plot(x, p, 'bo')
plt.tight_layout()
plt.show()
