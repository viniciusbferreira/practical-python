# pcost.py
#
# Exercise 1.33
import csv
import sys

def somar_preços(file):
    with open(file, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        soma = 0
        for row in rows:
            try:
                soma += float(row[2])
            except ValueError:
                print('Valor não encontrado.')
        return soma

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/missing.csv'

price = somar_preços(filename)
print('Total cost:', price)
