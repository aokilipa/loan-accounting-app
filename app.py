"""
->  The expectation is a file called Output.csv with a line detailing the totals by the tuple of
    (Network, Product, Month) summing the amount and count of loans.
->  A readme.txt detailing the project, usage and assumptions youʼve made as well as the
    choices around your language, plugins and 3rd party libraries.
->  Follow proper coding conventions, object orientated design.
->  Detail performance and scaling considerations.

"""

import csv


with open('Loans.csv','r') as fin, open('Output.csv','w') as fout:
    writer = csv.writer(fout, delimiter=',')
    for row in csv.reader(fin, delimiter=','):
        print (row)


def sort_by_month(parameter_list):
    return None

def sort_by_product(parameter_list):
    pass

def total(parameter_list):
    pass

 