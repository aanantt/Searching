def binary_search(s, ele):
    start = 0
    last = len(s) - 1
    while start <= last:
        mid = (start + last) // 2
        if ele == s[mid]:
            return "Element in the list"
        if ele > s[mid]:
            start = mid + 1
        else:
            last = mid - 1
    return "Not in the list"


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 8))
