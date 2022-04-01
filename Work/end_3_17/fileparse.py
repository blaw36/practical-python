# fileparse.py
#
# Exercise 3.3

import csv
from os import error
from typing import List

# Iteration 1
# def parse_csv(
#     filename: str
#     , select: List = None
#     , types: List = None
#     , has_headers: bool = True
#     , delimiter: str = ','
#     , silence_errors: bool = True):
#     '''
#     Parse a CSV file into a list of records
#     '''
#     if select and not has_headers:
#         raise RuntimeError("select argument requires column headers")

#     with open(filename) as f:
#         rows = csv.reader(f, delimiter=delimiter)

#         # If no headers, return some tuples
#         if not has_headers:
#             records = []
#             for row in rows:
#                 if not row:
#                     continue
#                 if len(row) == 0:
#                     continue
#                 if types:
#                     row = [func(val) for func, val in zip(types, row)]
#                 records.append(tuple(row))
#             return records

#         # Read the file headers
#         headers = next(rows)

#         # Check that select and types have compatible lengths
#         if not select:
#             select = headers
#         if (select and types) and (len(select) != len(types)):
#             raise ValueError("Number of type conversions not equal to number of columns selected")

#         # If column selector is there
#         if select:
#             indices = [headers.index(colnames) for colnames in select]
#             headers = select
#         else:
#             indices = []

#         records = []
#         for row_num,row in enumerate(rows):
#             try:
#                 if not row:
#                     continue
#                 if len(row) == 0:
#                     continue
#                 if indices:
#                     row = [row[index] for index in indices]
#                 if types:
#                     row = [func(val) for func, val in zip(types,row)]
                
#                 record = dict(zip(headers, row))
#                 records.append(record)

#             except ValueError as e:
#                 if not silence_errors:
#                     print("Row:",row_num,": Couldn't convert",row)
#                     print("Row:",row_num,":",e)

#     return records

# Iteration 2: more flexibility as per Ex 3.17
def parse_csv(
    file
    , select: List = None
    , types: List = None
    , has_headers: bool = True
    , delimiter: str = ','
    , silence_errors: bool = True):
    '''
    Parse a line (from an iterable file) and extract records
    '''
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")

    if isinstance(file, str):
        # Then it's a path, raise an error
        raise RuntimeError("file argument should be a file-like or iterable object, not a path")

    rows = csv.reader(file, delimiter=delimiter)

    # If no headers, return some tuples
    if not has_headers:
        records = []
        for row in rows:
            if not row:
                continue
            if len(row) == 0:
                continue
            if types:
                row = [func(val) for func, val in zip(types, row)]
            records.append(tuple(row))
        return records

    # Read the file headers
    headers = next(rows)

    # Check that select and types have compatible lengths
    if not select:
        select = headers
    if (select and types) and (len(select) != len(types)):
        raise ValueError("Number of type conversions not equal to number of columns selected")

    # If column selector is there
    if select:
        indices = [headers.index(colnames) for colnames in select]
        headers = select
    else:
        indices = []

    records = []
    for row_num,row in enumerate(rows):
        try:
            if not row:
                continue
            if len(row) == 0:
                continue
            if indices:
                row = [row[index] for index in indices]
            if types:
                row = [func(val) for func, val in zip(types,row)]
            
            record = dict(zip(headers, row))
            records.append(record)

        except ValueError as e:
            if not silence_errors:
                print("Row:",row_num,": Couldn't convert",row)
                print("Row:",row_num,":",e)

    return records

# import fileparse
# import gzip

# with gzip.open('Data/portfolio.csv.gz', 'rt') as file:
#     port = fileparse.parse_csv(file, types = [str,int,float])

# lines = ['name,shares,price', 'AA,100,34.23', 'IBM,50,91.1', 'HPE,75,45.1']
# port = fileparse.parse_csv(lines, types=[str,int,float])
