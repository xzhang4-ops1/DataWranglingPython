import csv
import pandas as pd

df_1 = pd.read_csv('datasets/data_wrangling_rl1_2021_u6906046.csv')
df_2 = pd.read_csv('datasets/data_wrangling_rl2_2021_u6906046.csv')
df_g = pd.read_csv('datasets/data_wrangling_rlgt_2021_u6906046.csv')
df_me = pd.read_csv('datasets/data_wrangling_rl_best_results_2021_u6906046.csv')
with open('datasets/data_wrangling_rl1_2021_u6906046.csv') as csvfile:
    reader = csv.reader(csvfile)
    rows_1 = [row for row in reader]

with open('datasets/data_wrangling_rl2_2021_u6906046.csv') as csvfile:
    reader = csv.reader(csvfile)
    rows_2 = [row for row in reader]
with open('datasets/data_wrangling_rlgt_2021_u6906046.csv') as csvfile:
    reader = csv.reader(csvfile)
    rows_gt = [row for row in reader]
with open('datasets/data_wrangling_rl_best_results_2021_u6906046.csv') as csvfile:
    reader = csv.reader(csvfile)
    rows_me = [row for row in reader]

list_concat_my = []
list_concat_grdountruth = []
list_l_first=[]
list_r_first=[]
count=0


for i in range(1,rows_1.__len__()):
    list_l_first.append(rows_1[i][0])
for i in range(1,rows_2.__len__()):
    list_r_first.append(rows_2[i][0])

for i in rows_me:
    str1 = i[0].title() + ','+i[1][1:].title()
    list_concat_my.append(str1)

for i in rows_gt:
    str1 = i[0].title() + ','+i[1].title()
    list_concat_grdountruth.append(str1)

for i in list_concat_grdountruth:
    if not list_concat_my.__contains__(i):
        count=count+1
        list_cotain=i.split(',')
        indexa=list_l_first.index(list_cotain[0])+1
        indexb = list_r_first.index(list_cotain[1])+1
        print(indexa,indexb)
        print(rows_1[indexa])
        print(rows_2[indexb])



#
print(count)
