import requests
from datetime import date

num_of_rows = input('Enter the number of rows: ')

p_list = requests.get('https://baconipsum.com/api?type=meat-and-filler').json()[:int(num_of_rows)]
reverse_p_list = p_list[::-1]

match_p_count = 0
str_of_p = ''
for p in reverse_p_list:
    str_of_p = str_of_p + '\n' + p
    if 'Pancetta' in p:
        match_p_count = match_p_count + 1

with open('output.txt', 'w') as file:
    to_write = ['Dmytro\n', str(date.today()), '\n', str(match_p_count), str_of_p]
    file.writelines(to_write)