
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)

# Ex 2.1
import csv
f = open('Data/portfolio.csv')
rows = csv.reader(f)
next(rows)
row = next(rows)
row
cost = row[1]*row[2]
t = (row[0], int(row[1]), float(row[2]))
t
cost = t[1]*t[2]
cost
print(f'{cost: 0.2f}')
print(f'{cost}')

# Tuples are read only
t[1] = 75
t = (t[0], 75, t[2])
t

name, shares, price = t
name
shares
price

t = (name, 2*shares, price)
t

d = {'name': row[0], 'shares': int(row[1]), 'price': float(row[2])}
d

cost = d['shares']*d['price']
cost

# dictionaries can be modified
d['shares'] = 75
d

d['date'] = (6, 11, 2007)
d['account'] = 12345
d

# Listing a dictionary returns all of its keys:
list(d)
for k in d:
    print('k =', k)

for k in d:
    print(k, '=', d[k])

keys = d.keys()
del d['account']
keys
list(keys)

items = d.items()
items
for k,v in d.items():
    print(k, '=', v)

items
new_dict = dict(items)
new_dict
