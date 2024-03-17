immutable_var=(1,7.6,'Denis', False, [1,9,7,8])
print(immutable_var)
immutable_var[2].replace('s','')
print(immutable_var) # Строка в кортеже не изменилась ?
immutable_var[4][2]=5
print(immutable_var) # Список в кортеже изменился

mutable_list=[1,7.6,'Denis', False, [1,9,7,8]]
print(mutable_list)
mutable_list[2]=mutable_list[2].replace('s','')
print(mutable_list) # Строка в списке изменилась
mutable_list[4][2]=5
print(mutable_list) # Список в списке именился