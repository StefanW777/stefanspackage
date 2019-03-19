def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''

    # Two consecutiove loops to bubble sort array
    for x in range(len(items)):
        for y in range(len(items)-1-x):
            if items[y] > items[y+1]: # Condition for swapping items
                items[y], items[y+1] = items[y+1], items[y]     # Swap!
    return items


def merge_sort(items):

    '''Return array of items, sorted in ascending order'''

    # Create condition incase length of itmes is 1
    len_items = len(items)
    if len_items == 1:
        return items

    # Get midpoint of len_items and use it to half lists
    mid_point = int(len_items / 2)
    I = merge_sort(items[:mid_point])
    J = merge_sort(items[mid_point:])


    sorted_items = []

    while len(I) > 0 and len(J) > 0: # Both must not be empty.

        # Comparing the first items in each, pop smallest item and append to new list
        if I[0] < J[0]:
            sorted_items.append(I.pop(0))

        else:
            sorted_items.append(J.pop(0))

    if len(I) == 0:
        sorted_items += J
    if len(J) == 0:
        sorted_items += I

    return sorted_items


def quick_sort(items):

    '''Return array of items, sorted in ascending order'''

    len_items = len(items)

    if len_items <= 1:
        return items

    pivot = items[-1]
    smaller = []
    larger = []
    copy = []
    for a in items:
        if a < pivot:
            smaller.append(a)
        elif a > pivot:
            larger.append(a)
        elif a == pivot:
            copy.append(a)

    smaller = quick_sort(smaller)
    larger = quick_sort(larger)

    return smaller + copy + larger
