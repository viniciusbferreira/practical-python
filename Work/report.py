# report.py
#
# Exercise 2.4
import csv
from pprint import pprint

def read_portfolio():
    '''Coloca um portfolio de ações em dicionários'''
    portfolios = []

    with open('Data/portfolio.csv', 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            portfolio = {}
            portfolio['name'] = row[0] 
            portfolio['shares'] = int(row[1])
            portfolio['price'] = float(row[2])
            portfolios.append(portfolio)
    return portfolios

def read_prices():
    '''Coloca os preços das ações em dicionários'''
    prices = {}

    with open('Data/prices.csv') as f:
        rows = csv.reader(f)
        for row in rows:
            if row:
                prices[row[0]] = row[1]
        return prices

def make_report(portfolios, prices):
    for i in portfolios:
        for k, v in prices.items():
            if i['name'] == k:
                i['change'] = float(v) - i['price']
    # Construct tuple from dictionary values
    report = [(d['name'], 
               d['shares'],
               d['price'],
               d['change']) for d in portfolios]

    return report

def add_currency(x):
    x = f'{x:.2f}'
    return '$' + str(x)

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    for h in headers:
        print(f'{h:>10s}', end=' ')
    print('\n---------- ---------- ---------- -----------')
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {add_currency(price):>10} {change:>10.2f}')

report = make_report(read_portfolio(), read_prices())
print_report(report)