# report.py
#
# Exercise 2.4

import csv
from fileparse import parse_csv

def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = []

    # with open(filename, 'rt') as f:
    #     rows = csv.reader(f)
    #     headers = next(rows)
    #     for row in rows:
    #         record = dict(zip(headers,row))
    #         # holding = (row[0], int(row[1]), float(row[2]))
    #         holding = {'name': record['name'], 'shares': int(record['shares']), 'price': float(record['shares'])}
    #         portfolio.append(holding)
    with open(filename, 'rt') as f:
        portfolio = parse_csv(f, select = ['name','shares','price'], types = [str,int,float])
    return portfolio

def read_prices(filename):
    '''Gets stock price name and prices and saves as dictionary'''
    # stocks = {}
    # with open(filename, 'rt') as f:
    #     rows = csv.reader(f)
    #     # headers = next(rows)
    #     for row in rows:
    #         if len(row) > 0:
    #             stocks[row[0]] = float(row[1])
    with open(filename, 'rt') as f:
        stocks_list = parse_csv(f, has_headers=False, types = [str,float])

    stocks = {ticker:price for ticker, price in stocks_list}
    return stocks

def gain_loss(portfolio_dict, price_list):
    current_value = 0.0
    gain_loss = 0.0

    for stock in portfolio_dict:
        stock_name = stock['name']
        curr_price = price_list.get(stock_name,None)
        if curr_price is not None:
            current_value += curr_price * stock['shares']
            gain_loss += (curr_price - stock['price']) * stock['shares']

    return {'current_value': current_value, 'gain_loss': gain_loss}

def make_report(portfolio_dict, price_list):
    # add price change
    new_list = portfolio_dict
    current_prices = [price_list[d['name']] for d in portfolio_dict]
    new_list = [dict(i[1], **{'current_price':i[0]}) for i in zip(current_prices,new_list)]
    report_tuple = [(i['name'],i['shares'],i['current_price'],i['current_price'] - i['price']) for i in new_list]
    return report_tuple

def print_report(pretty_report_tuples, headers = ('Name', 'Shares', 'Price', 'Change')):
    print('%10s %10s %10s %10s' % headers)
    print(f'{"":->10s} {"":->10s} {"":->10s} {"":->10s}')
    for name,shares,price,change in pretty_report_tuples:
        # print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
        formatted_price = '$' + '%.2f' % price
        print(f'{name:>10s} {shares:>10d} {formatted_price:>10s} {change:>10.2f}')

def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = gain_loss(portfolio, prices)
    pretty_report = make_report(portfolio, prices)
    print_report(pretty_report)

def main(argv):
    portfolio_report('Data/portfolio.csv', 'Data/prices.csv')

if __name__ == '__main__':
    import sys
    main(sys.argv)

# for r in pretty_report:
#     # print(r)
#     print('%10s %10d %10.2f %10.2f' % r)

# for name,shares,price,change in pretty_report:
#     print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

# from collections import Counter
# holdings = Counter()
# for s in portfolio:
#     holdings[s['name']] += s['shares']
# holdings.most_common()

# portfolio2 = read_portfolio('Data/portfolio2.csv')
# holdings2 = Counter()
# for s in portfolio2:
#     holdings2[s['name']] += s['shares']

# holdings2 + holdings