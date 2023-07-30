* Напишите программу, которая принимает две строки вида “a/b” - 
* дробь с числителем и знаменателем. Программа должна возвращать 
* сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

def gcd(x, y): 
    if(y == 0):
        return x
    else: 
        return gcd(y, x % y) 
 
def add(ch1, zn1, ch2, zn2):
    ch_new = ch1 * zn2 + zn1 * ch2
    zn_new = zn1 * zn2
    nod = gcd(ch_new, zn_new)
    return ([ch_new//nod, zn_new//nod])
    
def mult(ch1, zn1, ch2, zn2):
    ch_new = ch1 * ch2
    zn_new = zn1 * zn2
    nod = gcd(ch_new, zn_new)
    return ([ch_new//nod, zn_new//nod])

ch1, zn1 = (list(map(int, input('Первая дробь: ').split('/'))))
ch2, zn2 = (list(map(int, input('Вторая дробь: ').split('/'))))
print('Результат сложения:', '/'.join(map(str, (add(ch1, zn1, ch2, zn2)))))
print('Результат умножения:','/'.join(map(str, (mult(ch1, zn1, ch2, zn2)))))