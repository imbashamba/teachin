# Задача 1. Даны два списка, нужно вернуть элементы, которые есть в 1-ом списке, но нет во 2-ом. Оценить эффективность своего решения.
li_one = [3, 2, 1, 5, 0, 1, 7]
li_two = [3, 6, 4, 2, 0]

result = list(set(li_one)-set(li_two)) # сложность от O(n) до O(n^2) в худшем случае
print (result) 


# Задача 2. Дан массив целых чисел. Нужно удалить из него нули. Можно использовать только О(1) дополнительной памяти
li = [0, 1, 0, 0, 4, 5, 6, 7, 0, 8]
while True:
    try:
        li.remove(0)
    except Exception:
        break
print(li)
