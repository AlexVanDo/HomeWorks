from pprint import pprint
import re
import csv

with open("Regular Expressions/phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)

for id_, data in enumerate(contacts_list):
  for name in data[:3]:
    if len(name.split(' ')) == 3:
      
      last_name = name.split(' ')[0]
      first_name = name.split(' ')[1]
      surname = name.split(' ')[2]

      contacts_list[id_][0] = last_name
      contacts_list[id_][1] = first_name
      contacts_list[id_][2] = surname

    if len(name.split(' ')) == 2:
      last_name = name.split(' ')[0]
      first_name = name.split(' ')[1]

      contacts_list[id_][0] = last_name
      contacts_list[id_][1] = first_name
      
for id_, data in enumerate(contacts_list):

  number = data[5]
  result = re.sub('[\s,(,),-]', '', number)

  if len(result) <= 12 and 'phone' not in result and result:
    pat = re.compile(r'(7|8|\+7)(\d{3})(\d{3})(\d{2})(\d{2})')
    sub_pat = r'+7(\2)\3-\4-\5'
    result = pat.sub(sub_pat, result)

  else:
    if result == 'phone' or len(result) < 12 :continue
    result = re.split('доб.', result)
    pat = re.compile(r'(7|8|\+7)(\d{3})(\d{3})(\d{2})(\d{2})')
    sub_pat = r'+7(\2)\3-\4-\5'
    result_num = pat.sub(sub_pat, result[0])
    result = result_num + ' доп.' + result[1]

  contacts_list[id_][5] = result

text = ''
for id_, data in enumerate(contacts_list[1:]):
  for element in data:
    if element: text += element + ' '
duplicate_list = []
for id_, data in enumerate(contacts_list):
  duplicate_id = [0]
  name = data[0]
  last_name = data[1]
  name_list = re.findall(fr'({name} {last_name})', text)
  if len(name_list)>1:
    duplicate_id = [name_list, id_]
    duplicate_list.append(duplicate_id)

for_remove = []
for num, duplic_elem in enumerate(duplicate_list):
  if num + 2 <= len(duplicate_list) and duplicate_list[num][0] == duplicate_list[num+1][0]:
    elem_1 = duplicate_list[num][1]
    elem_2 = duplicate_list[num+1][1]
    for_remove.append(elem_2)
    for num, _ in enumerate(contacts_list[elem_1]):
      if bool(contacts_list[elem_1][num]) == False:
        contacts_list[elem_1][num] = contacts_list[elem_2][num]
count = 0
for remove_elem in for_remove:
  num = remove_elem - count
  contacts_list.remove(contacts_list[num])
  count += 1

with open("Regular Expressions/phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)