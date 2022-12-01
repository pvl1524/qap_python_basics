num, data_original = 0, [] #Инициализация переменных

data = list(map(int, input("Введите последовательность чисел через пробел: ").split()))

num = int(input("Введите число: "))

data.append(num) # Добавить введенное число num в конец исходной последовательности

# Функция сортировки списка чисел по возрастанию
def my_list_sort(list_):
    return sorted(list_)

data_sort = my_list_sort(data)

# Функция бинарного поиска индекса числа
def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует
    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

# Проводить поиск индекса, если введенное число > минимального и <= максимального в отсортированной последовальности
if num > min(data_sort) and num <= max(data_sort[:-1]):
    res = binary_search(data_sort, num, 0, len(data_sort) - 1)
    idx_min = res - 1
    idx_max = res + 1
    print(f"Индекс числа, которое меньше заданного num = {num}, равен {idx_min}, число {data_sort[idx_min]}")
    print(f"Индекс числа, которое больше или равно заданному num = {num}, равен {idx_max}, число {data_sort[idx_max]}")

elif num <= min(data_sort): # Если введенное число num <= минимального в отсортированной последовальности
    print(f"Число меньше, чем введенное num = {num}, отсутствует в последовательности. Индекс числа больше введенного равен 1 "
          f"(в отсортированной последовательности с включением чмсла num)")

elif num > max(data_sort[:-1]): #Если введенное число num > максимального в отсортированной последовальности. Из сравнения исключается само число num
    idx_max_r = len(data_sort) - 2  # Индекс последнего (не включая num) числа в списке data_sort (если введено число num больше максимального в списке data_sort)
    print(f"Индекс макс числа {idx_max_r}")
    print(f"Индекс числа меньше, чем введенное, равен {idx_max_r}. Число >= введенного (num = {num}) отсутствует в последовательности")
