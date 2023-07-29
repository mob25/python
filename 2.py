* Напишите программу, которая получает целое число и возвращает его 
* шестнадцатеричное строковое представление. Функцию hex используйте
* для проверки своего результата.


num = int(input())
hex_list = "0123456789ABCDEF"
hex_result = []

while num > 0:
    remainder = num % 16
    hex_result.insert(0, hex_list[remainder])
    num = num // 16
print(''.join(hex_result))