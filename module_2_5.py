def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        empty_list = []
        matrix.append(empty_list)
        for j in range(m):
            empty_list.append(value)
    return matrix

n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))
value = input('Введите число: ')
result = get_matrix(n, m, value)
print(result)

if n <= 0 or m <=0:
    print('Задан аргумент(ы) со значением 0 или меньше')
    result.clear()