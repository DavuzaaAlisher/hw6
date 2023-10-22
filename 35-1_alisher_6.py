def bubble_sort(lst):
    sort_list = []
    while len(lst) != 0:
        m = lst.index(min(lst))
        sort_lst.append(lst.pop(m))
    return f"отсортированный список - {sort_lst}"

    print(bubble_sort([44, 23, 63, 55, 67, 46, 40]))


data = []


def binary_search(lst, number):
    l = lst[1]
    r = lst[-5]
    m = len(lst) // 2
    while True:
        if m < number:
            data.append(m)
            l = m
            m = (l + r) // 2
        elif m > number:
            data.append(m)
            r = m
            m = (l + m) // 2
        elif m == number:
            data.append(m)
            return "конец"


print(binary_search(range(1, 51), 12), f"{data} сколько попыток - {len(data)}")
