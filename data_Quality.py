import pandas as pd
import script_Data


def tempo(str1):
    # 0: rec_id
    #  1: first_name
    #  2: middle_name
    #  3: last_name
    #  4: gender
    #  5: current_age
    #  6: birth_date
    #  7: street_address
    #  8: suburb
    #  9: postcode
    # 10: state
    # 11: phone
    # 12: email
    list_count_error = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    list_orror_word = ['rid', 'first_name', 'middle_name', 'last_name', 'gender', 'current_age', 'birth_date',
                       'street_address', 'suburb', 'postcode', 'state', 'phone', 'email']

    df_cleana = pd.read_csv('datasets/data_wrangling_rl1_2021_u6906046.csv')
    datastr2 = str1
    dfmy1 = pd.read_csv(datastr2)
    print(dfmy1.isnull().sum())
    rows = script_Data.opencsv_1(datastr2)
    cc = 0
    for i in range(1, rows.__len__()):

        firstname = rows[i][1]
        middlename = rows[i][2]
        lastname = rows[i][3]
        birthdate = rows[i][6]
        street = rows[i][7]
        suburb = rows[i][8]
        postcode = rows[i][9]
        phone = rows[i][11]
        email = rows[i][12]

        if script_Data.name(firstname) == False:
            # print(firstname)
            list_count_error[1] = list_count_error[1] + 1
        if script_Data.name(middlename) == False:
            # print(middlename)  # 3 wrong all have numbers
            list_count_error[2] = list_count_error[2] + 1
        if script_Data.name(lastname) == False:
            list_count_error[3] = list_count_error[3] + 1
            # print(lastname)  # only one havs symbol
        if script_Data.birthdate(birthdate) == False:
            list_count_error[6] = list_count_error[6] + 1
            # print(birthdate)
        if street == '':
            cc = cc + 1
        if script_Data.street_address(street) == False:
            list_count_error[7] = list_count_error[7] + 1
            # if street!='':
            #     print(street)
        if script_Data.street_address(suburb) == False:
            list_count_error[8] = list_count_error[8] + 1
            # print(suburb)
        if script_Data.postcode(postcode) == False:
            list_count_error[9] = list_count_error[9] + 1
            # print(postcode)
        if script_Data.phone(phone) == False:
            list_count_error[11] = list_count_error[11] + 1
            # print(phone)
        if script_Data.email(email) == False:
            list_count_error[12] = list_count_error[12] + 1
            # print(email)

    return list_count_error







""" Module with functionality to save the linkage results to a CSV file.
"""

# =============================================================================
# Import necessary modules

import os

# -----------------------------------------------------------------------------

def save_linkage_set(file_name, class_match_set):
  """Write the given set of matches (record pair identifiers) into a CSV file
     with one pair of record identifiers per line)

     Parameter Description:
       file_name       : Name of the data file to be write into (a CSV file)
       class_match_set : The set of classified matches (pairs of record
                         identifiers)
  """

  out_f = open(file_name, 'w')  # Open a CSV file for writing

  print('Write linkage results to file: '+file_name)

  for (rec_id1, rec_id2) in sorted(class_match_set):  # Sort for nicer output

    out_line = '%s, %s' % (rec_id1, rec_id2)

    out_f.write(out_line + '\n')

  out_f.close()

  print('  Wrote %d linked record pairs' % (len(class_match_set)))
  print('')

# -----------------------------------------------------------------------------

# End of program.

