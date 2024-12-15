data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
Summ=0
s=0
t=[0]

def extract_values(data):# Извлечение вложенных значений из строк и суммирование значений
    result = []
    summ1=[]
    summ=0
    if isinstance(data, (list, tuple, set,dict)):
         for item in data:
            if isinstance(data,dict):
                for keys,values in data.items():
                    result.append(keys)
                    result.append(values)
                break
            else:
                result.extend(extract_values(item))
    else:
        result.append(data)
    for i in result:
        if isinstance(i,int):
            summ+=i
        else:
            summ=summ+len(i)
    summ1.append(summ)
    return summ1

for j in data_structure:
    if type(j)==str:
        Summ=(Summ+len(j))
    else:
        t=extract_values(j)
        for value in t:
            Summ+=value
print(Summ)

