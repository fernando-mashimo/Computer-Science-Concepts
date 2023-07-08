# def quicksort(list):
#     if len(list) < 2:
#         return list

#     else:
#         pivot = list.pop(0)
#         higher = []
#         lower = []
#         for item in list:
#             lower.append(item) if item <= pivot else higher.append(item)
#         return quicksort(lower) + [pivot] + quicksort(higher)


def find_duplicate(nums):
    if len(nums) <= 1 or isinstance(nums, str):
        return False

    # nums_sorted = quicksort(nums)
    # for index, num in enumerate(nums_sorted[:-1]):
    #     if not isinstance(num, int) or num <= 0:
    #         return False
    #     elif num == nums_sorted[index + 1]:
    #         return num

    found_numbers = set()
    for num in nums:
        if not isinstance(num, int) or num <= 0:
            return False
        if num in found_numbers:
            return num
        found_numbers.add(num)

    return False
