#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import argparse

def year_to_numbers(year):
    """
    Convert the given year into an array of digits.

    e.g. year_to_numbers(1990) -> [1, 9, 9, 0]
    """
    result = []
    for i in 1000,100,10,1:
        result.append(int(year / i))
        year = year % i
    return result

def numbers_to_single(numbers):
    """
    Summarize the digits of the given input array.
    The output number is always between 1 and 9.
    
    e.g. numbers_to_single([1,9,9,0]) -> 1
    """
    res = sum(numbers)
    while res >= 10:
        res = sum(numbers)
        numbers = year_to_numbers(res)
    return res

def year_basenum(original_year):
    """
    Return the sum of digits of a given year.
    Wrapper function to use year_to_numbers and numbers_to_single together.

    e.g. year_basenum(1990) -> 1
    """
    return numbers_to_single(year_to_numbers(original_year))

def milestones(born, limit=80):
    """
    Calculate the actual milestone dates.

    Arguments:
    born -- The given year to calculate milestones from.
    limit -- An upper limit of years to calculate results to. By setting
    it to 80 years, it tipically covers most of our lifespans.
    """
    year = born
    ret = []

    while year <= born + limit:
        year += year_basenum(year)
        ret.append(year)

    return ret

def main(args):
    """
    Main function.
    """
    
    # Error checking
    if args.birth_year <= 0:
        print('You entered incorrect birth year.')
        return
    
    print('You were born in', args.birth_year)
    print('Your Master Number is', year_basenum(args.birth_year))

    print('Your milestone years are:')
    for year in milestones(args.birth_year):
        print(' ', year)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate milestone years in your life.')
    parser.add_argument('birth_year', type=int, help='Your birth year.')

    args = parser.parse_args()

    main(args)
