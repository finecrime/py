# Вводим последовательность чисел [16 20 42 4 8 15] и проверка соответствия условию
array = input("Введите последовательность чисел через пробел:").split()
array_1 = list(map(int, array))

print(type(array_1))


#Сортировка списка по возрастанию элементов в нем, метод Сортировка пузырьком

for i in range(len(array_1)):
    for j in range(len(array_1) - i - 1):
        if array_1[j] > array_1[j + 1]:
            array_1[j], array_1[j + 1] = array_1[j + 1], array_1[j]

print(array_1)

#Устанавливается номер позиции элемента, который меньше введенного пользователем числа,
# а следующий за ним больше или равен этому числу. Метод алгоритм двоичного поиска

def binary_search(array_1, number, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array_1[middle] == number:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif number < array_1[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array_1, number, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array_1, number, middle + 1, right)

number = int(input('Введите любое число:   '))
array_1 = [i for i in range(number)]

#запускаем алгоритм на левой и правой границе
print(binary_search(array_1, number, array_1[0], array_1[-1]))