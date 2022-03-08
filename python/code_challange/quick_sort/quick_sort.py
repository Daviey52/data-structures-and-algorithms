def quick_sort(array1):
    length = len(array1)
    if length <=1:
        return array1
    else:
        pivot = array1.pop()

    items_greater =[]
    items_smaller = []

    for item in array1:
        if item> pivot:
            items_greater.append(item)
        else:
            items_smaller.append (item)
    return quick_sort(items_smaller) + [pivot] + quick_sort(items_greater)

# print(quick_sort([8,4,23 ,42,16 ,15]))





