def quick_sort(s):
    if len(s) <= 1:
        return s
    elem = s[0]
    left = list(filter(lambda x: x < elem, s))
    center = [i for i in s if i == elem]
    right = list(filter(lambda x: x > elem, s))

    return quick_sort(left) + center + quick_sort(right)

s = [9, 5, 6, 4, 2, 1, 3, 7, 8]
print(quick_sort(s))
