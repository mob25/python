* Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
* Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть 
* один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.


things = dict(палатка = 10, вода = 3, спальник = 5, аптечка = 1,
              еда = 8, посуда = 4, коврик = 1, одежда = 2)
weight_limit = int(input('Максимальный вес рюкзака: '))
list_things = list(things.keys())
res, temp_list, current_weight = set(), [], 0
              
for i in range((2**len(things))):
    sample = (list(bin(i)[2:].zfill(len(things))))
    for n in range(len(sample)):
        if sample[n] == '1':
            temp_list.append(list_things[n])
            current_weight += things[list_things[n]]
            if current_weight > weight_limit:
                temp_list.pop()
                break
    res.add(' '.join(temp_list))
    temp_list, current_weight = [], 0

print('Все варианты комплектации рюкзака:')
for i in sorted(res):
    print(i)