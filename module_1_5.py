immutable_var=1,1.7,"CHeburek",True #кореж с типами
print("Immutable tuple:",(immutable_var), type(immutable_var))#вывод кортежа и его типа
#immutable_var[2]='Гоги'
#print("Immutable tuple:",(immutable_var), type(immutable_var))
mutable_list="varp",[23,87,34,1],"super_varp",3.14# кортеж со списком
print("Mutable list:",(mutable_list), type(mutable_list))
mutable_list[1][1]=98#замена элемента в списке
mutable_list[1][3]=5#замена элемента в списке
print("Changed mutable_list:",(mutable_list), type(mutable_list))
