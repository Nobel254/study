
def  custom_write(file_name, strings):
    file=open(file_name,'w',encoding='UTF-8')
    spis_cord=[]
    spis_item=[]
    for i in range (len(strings)):
        spis_cord.append(((i+1),file.tell()))
        file.write((strings[i])+'\n')
        spis_item.append(strings[i])
    file.close()
    strings_positions=dict(zip(spis_cord,spis_item))
    return strings_positions



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
