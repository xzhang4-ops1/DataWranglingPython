import pandas as pd
import csv
import re


def find_num(str1):
    bo = False
    for i in str1:
        if i.isdigit():
            bo = True
            break
    return bo


def find_alpha(str1):
    bo = False
    for i in str1:
        if i.isalpha():
            bo = True
            break
    return bo


def opencsv_1(str):
    with open(str) as csvfile:
        reader = csv.reader(csvfile)
        rows_1 = [row for row in reader]

    return rows_1


def street_address(str1):
    peratece = False
    bo = True
    if str1 == '':
        return False
    if str1.__contains__('-'):
        str1 = str1.replace('-', '')
    if str1.__contains__("("):
        str1 = str1.replace("(", '')
        if str1.__contains__(')'):
            str1 = str1.replace(')', '')
            peratece=True
    if str1.__contains__('of'):
        str1 = str1.replace('of', '')
    if str1.__contains__('&'):
        str1 = str1.replace('&', '')
    if str1 != '':
        list_spli = str1.split(' ')
        for i in list_spli:
            if i != '':
                if not i.isdigit() and not i.isalpha():
                    if not i.__contains__("'") and not i.__contains__('-'):
                        bo = False
                        break
                    elif i.__contains__("'"):
                        index1 = i.index("'")
                        if index1 < i.__len__():
                            aftersymbol = i[index1 + 1:]
                            if aftersymbol!='':
                                if aftersymbol[0] != 's' and not aftersymbol.istitle():
                                    bo = False
                                    break
                        else:
                            bo = False

            if not peratece:
                if i.isalpha():
                    if not i[0].isupper():
                        bo = False
    else:
        bo = False

    return bo


# print(street_address(sss))

sss = "alli-balogun"


def name(str):
    bo = True
    if str == '':
        return False
    if str.__contains__("("):
        str = str.replace("(", '')
    if str.__contains__(')'):
        str = str.replace(')', '')
    if str.__contains__("'"):
        str = str.replace("'", '')
    if str.__contains__('-'):
        str = str.replace("-", '')
    if str.__contains__('/'):
        str = str.replace('/', '')

    if not str.isalpha():
        bo = False

    return bo


def birthdate(str):
    bo = True
    if str == '':
        return False
    listb = str.split('/')
    for i in listb:
        if not i.isdigit():
            bo = False
    return bo


def email(addr):
    if addr == '':
        return False
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.fullmatch(regex, addr)):
        bo = True
    else:
        bo = False
    return bo


def postcode(str):
    bo = True
    if str == '':
        return False
    elif not str.isdigit():
        bo = False
    return bo


def phone(str1):
    bo = True
    if str1 == '':
        return False
    listph = str1.split('  ')
    # print(listph)
    for i in listph:
        if not i.isdigit():
            bo = False
            break
    return bo
