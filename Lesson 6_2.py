# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше
# заданного максимума)

def find_indexes(lst, min_val, max_val):
    indexes = []
    for i, val in enumerate(lst):
        if min_val <= val <= max_val:
            indexes.append(i)
    return indexes
