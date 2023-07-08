def quicksort(list):
    if len(list) < 2:
        return list

    else:
        pivot = list.pop(0)
        higher = []
        lower = []
        for item in list:
            lower.append(item) if item <= pivot else higher.append(item)
        return quicksort(lower) + [pivot] + quicksort(higher)


def is_anagram(first_string, second_string):
    first_sorted = ''.join(quicksort(list(first_string.lower())))
    second_sorted = ''.join(quicksort(list(second_string.lower())))
    if len(first_sorted) == 0 or len(second_sorted) == 0:
        return (first_sorted, second_sorted, False)
    else:
        return (first_sorted, second_sorted, first_sorted == second_sorted)
