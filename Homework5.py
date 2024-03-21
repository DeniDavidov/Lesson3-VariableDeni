my_list=['яблоко','персик','вишня','банан','кокос','ананас']  # Списки (класс List)
print(my_list)
print (my_list[0])
print (my_list[5])
print(my_list[2:5])
my_list [5] = 111
print(my_list)
my_dict = {'apple': 'яблоко', 'int': 'целые', 1: 'еденица', 'my_list': my_list} # Словари (класс Dict)
print(my_dict)
print(my_dict['my_list'])
my_dict [3.14] = 'ПИ'
print(my_dict)
my_list_2 = [2,0,2,4]
my_dict ['my_list'] = my_list_2
print(my_dict)
print(type(my_dict))