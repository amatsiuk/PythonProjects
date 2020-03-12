def main():

    arr = [10,20,30,40,50]
    #print(arr[-1])      # вывод последней ячейки
    #arr[2] = 13          # перезаписали ячейку
    #arr.append(1300)     # добавили значение в конец списка
    for i in range(5):
        arr.append(i)
    arr.insert(2,100)
    arr.remove(0)
    #arr.sort()
    sort_arr = sorted(arr)
    print(len(arr))
    for x in arr:
        #print(x)
        print(x, end=", ")
    for x in sort_arr:
        print(x, end=", ")

    create_odd_list()


def create_odd_list():
    arr_positive = []  # создаем список
    for x in range(-10, 10, 1):  # генерируем значения
        if x % 2 == 1:  # проверяем условие (четные, нечетные)
            arr_positive.append(x)  # добавлеям в список
    for item in arr_positive:
        print(item, end=", ")

    values = []
    for i in range(10):
        value = int(input("Enter int value"))
        values.append(value)
    print(values)


if __name__ == "__main__":
    main()

