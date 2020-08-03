import requests
import json
import sys
import hidden
from datetime import datetime, timedelta


ETFs = ['SPY', 'SH', 'VXX', 'EEM', 'QQQ', 'PSQ', 'XLF', 'GDX', 'HYG', 'EFA', 'IAU', 'XOP', 'IWM', 'FXI', 'SLV', 'USO', 'XLE', 'IEMG', 'AMLP', 'EWZ', 'XLK', 'XLI', 'VWO', 'GLD', 'XLP', 'JNK', 'EWJ', 'XLU', 'VEA', 'IEFA',
        'XLV', 'PFF', 'VIXY', 'TLT', 'GDXJ', 'LQD', 'XLB', 'BKLN', 'XLY', 'SMH', 'OIH', 'ASHR', 'RSX', 'MCHI', 'VTI', 'EWH', 'SPLV', 'KRE', 'IVV', 'DIA', 'IEF', 'EZU', 'EWT', 'SPDW', 'VOO', 'SCHF', 'EWY', 'MYY', 'DOG', 'EUM']

for ticker in ETFs:
    period = 365
    endDate = datetime.today().strftime('%Y-%m-%d')
    startDate = (datetime.today() - timedelta(days=period)
                 ).strftime('%Y-%m-%d')
    url = "https://api.tiingo.com/tiingo/daily/%s/prices?startDate=%s&endDate=%s" % (
        ticker, startDate, endDate)

    response = requests.get(url, cookies=hidden.cookies)
    jsonData = {}

    if response.status_code == 200:
        jsonData = json.loads(response.text)

        if jsonData:
            filename = '%s_%s_%s.txt' % (ticker, startDate, endDate)
            f = open(filename, "w")
            f.write('Date,Open,High,Low,Close,Adj Close,Volume\n')

            for data in jsonData:
                f.write(data['date'][0:10] + ',' + str(data['open']) + ',' + str(data['high']) + ',' + str(data['low'])
                                           + ',' + str(data['close']) + ',' + str(data['adjClose']) + ',' + str(data['volume']) + '\n')

            f.close()
            print('file: %s created' % filename)



