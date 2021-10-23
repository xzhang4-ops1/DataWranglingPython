import csv

with open('datasets/data_wrangling_rl1_2021_u6906046.csv') as csvfile:
    reader = csv.reader(csvfile)
    rows_1 = [row for row in reader]

with open('datasets/data_wrangling_rl2_2021_u6906046.csv') as csvfile:
    reader = csv.reader(csvfile)
    rows_2 = [row for row in reader]
with open('datasets/data_wrangling_rlgt_2021_u6906046.csv') as csvfile:
    reader = csv.reader(csvfile)
    rows_gt = [row for row in reader]

attris = rows_2[0]

list_count_error = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
list_orror_word = ['first_name', 'middle_name', 'last_name', 'gender', 'current_age', 'birth_date', 'street_address',
                   'suburb', 'postcode', 'state', 'phone', 'email']

print(list_count_error.__len__())
print(list_orror_word.__len__())
print(attris)
print(list_count_error)
count = 0
print(rows_gt.__len__())
for i in range(0, rows_gt.__len__()):
    left_Index = rows_gt[i][0].title()
    right_Index = rows_gt[i][1]
    # right_Index = rows_gt[i][1][1:].title()  #for personal data
    cr = 0
    cl = 0
    for j in rows_1:
        if j[0] == left_Index:
            cl = j[1:]
            break
    for k in rows_2:
        if k[0] == right_Index:
            cr = k[1:]
            break
    if cl != cr:
        count = count + 1
        # print(cl)
        # print(cr)
        count_each = 0
        for f in range(0, cr.__len__()):
            if cl[f] != cr[f]:
                list_count_error[f] = list_count_error[f] + 1
                count_each = count_each + 1
        print("each have a different " + str(count_each))
for i in range(0, list_count_error.__len__()):
    print(list_orror_word[i] + " have a different value    " + str(list_count_error[i]))
