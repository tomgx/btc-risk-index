import time
import pickle
from datetime import datetime, timedelta
import dateutil.utils
from coinpaprika import client as Coinpaprika

client = Coinpaprika.Client()


class dates_generator:
    def __init__(self):
        print('Generating list of dates')

    def dates(self, start_date, end_date):
        start = datetime.strptime(start_date, '%Y%m%d')
        end = datetime.strptime(end_date, '%Y%m%d')
        step = timedelta(days=1)

        date_list = []
        while start <= end:
            date_list.append(start.date().strftime("%Y-%m-%d"))
            start += step
        print('Dates generated!\n')
        return date_list


current_date = dateutil.utils.today()

dates = dates_generator().dates('20101001', current_date.strftime("%Y%m%d"))


class data_generator: 
    def __init__(self):
        print('Generating BTC historical data')

    def data(self, dates):
        data = []
        print('Limited to 10 API call/s - may take some time to complete')
        for i in range(len(dates)):
            data.append(client.historical("btc-bitcoin", start=dates[i]))
            time.sleep(0.1)
        print('- Complete! -')
        return data


data = data_generator().data(dates)

with open("btc_price_history.txt", "wb") as fp:
    pickle.dump(data, fp)
