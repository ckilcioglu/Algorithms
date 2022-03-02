import math
import sys
import random


def merge(a, p, q, r):
    left = a[p:q+1]
    right = a[q+1:r+1]
    left.append(math.inf)
    right.append(math.inf)
    i = 0
    j = 0

    for k in range(p, r + 1):
        if left[i] < right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1


def merge_sort(a, start=0, end=0):
    if start < end:
        q = (start + end) // 2
        merge_sort(a, start=start, end=q)
        merge_sort(a, start=q + 1, end=end)
        merge(a, start, q, end)


if __name__ == "__main__":
    the_list = [random.randint(0, 1000) for i in range(100)]

#    merge([1, 2, 3, 4, 5, 6, 7, 8], 0, 4, 7)
#    sys.exit(0)

    print(f"List before sorting:\n{the_list}")
    merge_sort(the_list, start=0, end=len(the_list) - 1)
    print(f"List after sorting:\n{the_list}")
