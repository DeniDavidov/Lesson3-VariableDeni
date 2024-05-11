def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = [111, 'список_раз_из_трех', 11.333]
values_list_2 = [222, 'список_два_из_двух']
values_dict = {'a':5, 'b':'5_число_ПИ', 'c':3.14}


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42) # (c = 42, а не 'a')