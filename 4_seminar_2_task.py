* Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
* где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, 
* используйте его строковое представление.


def inverse_hash(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            result[value] = key
        except:
            result[str(value)] = key
    return result

print(inverse_hash(one = 1, two = ['2'], three = (3,)))