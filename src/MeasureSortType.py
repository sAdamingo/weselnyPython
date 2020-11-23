import time


def measure_sort_time(sorting_function, list):
    start_time = time.clock()
    sorting_function(list)
    return time.clock()-start_time


if __name__ == '__main__':
    arr = ['Marcin', 'Adam', 'Agata', 'Anna', 'Mateusz', 'Wojtek', 'Kasia', 'Tomek', 'Kamil', 'Maria', 'Arkadiusz', 'Przemysław', 'Horacy', 'Zofia', 'Genowefa', 'Serafin']
    sort_with_sorted = lambda add: sorted(add)
    sort_with_sort = lambda list: list.sort()
    print(measure_sort_time(sort_with_sort, arr))
    print(arr)
    arr = ['Marcin', 'Adam', 'Agata', 'Anna', 'Mateusz', 'Wojtek', 'Kasia', 'Tomek', 'Kamil', 'Maria', 'Arkadiusz', 'Przemysław', 'Horacy', 'Zofia', 'Genowefa', 'Serafin']
    print(measure_sort_time(sort_with_sorted, arr))
    print('this is not sorted because .sorted() do not change the referenced object')
    print(arr)