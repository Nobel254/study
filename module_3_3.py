def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
    print()

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list =["First", 2, [3, False]]
values_dict={'a':False,'b':56,'c':"Second"}
print_params(*values_list)
print_params(**values_dict)

values_list_2=["Third",[45,32]]
print_params(*values_list_2, 42)

