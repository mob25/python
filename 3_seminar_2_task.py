* Дан список повторяющихся элементов. Вернуть список с
* дублирующимися элементами. В результирующем списке 
* не должно быть дубликатов.


original_list = [2, 3, 5, 1, 2, 2, 5, 0, 5]
print(list(set([i for i in original_list if original_list.count(i) > 1])))