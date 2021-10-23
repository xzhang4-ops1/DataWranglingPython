import data_Quality
list_orror_word = ['rid', 'first_name', 'middle_name', 'last_name', 'gender', 'current_age', 'birth_date',
                       'street_address', 'suburb', 'postcode', 'state', 'phone', 'email']
str1='datasets/data_wrangling_rl1_2021_u6906046.csv'
str2='datasets/data_wrangling_rl2_2021_u6906046.csv'
lista=data_Quality.tempo(str1)
listb=data_Quality.tempo(str2)
listc=[]
for i in range(0,lista.__len__()):
    listc.append(lista[i]+listb[i])

for i in range(0, listc.__len__()):
    print(list_orror_word[i] + 'has ' + str(listc[i]) + " wrong values, ")