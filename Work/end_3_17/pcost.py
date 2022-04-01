# pcost.py
#
# Exercise 1.27

import csv
import sys
from report import read_portfolio

# import os
# os.chdir('C:\\Users\\brend\\Documents\\python\\practical-python\\Work')

# with open('Data\\portfolio.csv', 'rt') as f:
#     header = next(f)
#     cost = []
#     for line in f:
#         row = line.split(",")
#         row[1] = int(row[1])
#         row[2] = float(row[2].replace("\n",""))
#         cost.append(row[1] * row[2])

# print(f'Total cost: {round(sum(cost),2)}')

# import gzip
# with gzip.open('Data\\portfolio.csv.gz', 'rt') as f:
#     for line in f:
#         print(line, end='')

def portfolio_cost(filename):
    
    # with open(filename, 'rt') as f:
    #     rows = csv.reader(f)
    #     header = next(rows)
    #     total_cost = 0
    #     for row_num,row in enumerate(rows):
    #         record = dict(zip(header, row))
    #         try:
    #             nshares = int(record['shares'])
    #             price = float(record['price'])
    #             total_cost += nshares*price
    #         except ValueError:
    #             print(f"Row {row_num}: Couldn't convert: {row}")
    portfolio = read_portfolio(filename)
    total_cost = 0
    for share in portfolio:
        total_cost += share['shares']*share['price']

    return(round(total_cost, 2))

def main(argv):

    cost = portfolio_cost(argv[1])
    print('Total cost:', cost)

    # cost = portfolio_cost('Data/portfolio.csv')
    # print('Total cost:', cost)

    # cost = portfolio_cost('Data/missing.csv')
    # print('Total cost:', cost)

if __name__ == '__main__':
    import sys
    main(sys.argv)