* В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
* Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии 
* или из документации к языку.


import string
import itertools

line = "permutations(). Возвращает последовательные r перестановок элементов в итерируемом объекте. \
        Если параметр r не указан или стоит в значении None, то по умолчанию r принимает длину \
        итерируемого объекта и генерирует все возможные полноценные перестановки. Кортежи перестановок \
        выдаются в лексикографическим порядке в соответствии с порядком итерации входных данных. \
        Таким образом, если входные данные итерируемого объекта отсортированы, то комбинация кортежей \
        будет выдаваться в отсортированном порядке. Элементы рассматриваются как уникальные в зависимости \
        от их позиции, а не от их значения. Таким образом, если входные элементы уникальны, то в каждой \
        перестановке не будет повторяющихся значений."

line = ((line.translate(str.maketrans('', '', string.punctuation))).lower()).split()
d = dict()
for word in line:
    if word not in d:
        d[word] = 1
    else:
        d[word] = d[word] + 1
   
d = ({k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse = True)})
d = dict(itertools.islice(d.items(),10))
print(d)