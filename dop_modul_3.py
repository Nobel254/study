data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
Summ=0
def dict_(b):# Функция подсчёта суммы в словаре
    Summ_=0
    for i in b.values():
        if type(i)==int:
            Summ_=(Summ_+i)
        else:
            Summ_=Summ_+len(i)
    for i in b:
        if type(i)==int:
            Summ_=(Summ_+i)
        else:
            Summ_=Summ_+len(i)
    return Summ_
def vl(j): #Функция определения вложенности
    vl_ = sum(isinstance(l, (set, tuple, dict,)) for l in j)
    if vl_>0:
        return 1
    else:
        return 0
def extract_values(data):# Извлечение вложенных значений из строк
    result = []
    if isinstance(data, (list, tuple, set)):
        for item in data:
            result.extend(extract_values(item))
    else:
        result.append(data)
    return result

for j in data_structure:
    if type(j)==str:
        Summ=(Summ+len(j))
    if type(j)==list:
        Summ = (Summ + sum(j))
    if type(j)==dict:
        Summ = (Summ + dict_(j))
    if type(j)==tuple:
        print(f'extract_values= {extract_values(j)}')
        print(f'vl(extract_values(j)){vl(extract_values(j))}')
        if vl(extract_values(j))<1:
            for u in extract_values(j):
                if type(u)==int:
                    Summ+=u
                elif type(u)==str:
                    Summ = (Summ + len(u))
        else:
            for y in extract_values(j):
                if type(y) == int:
                    Summ += y
                elif type(y) == dict:
                    Summ = (Summ + dict_(y))

print(Summ)

