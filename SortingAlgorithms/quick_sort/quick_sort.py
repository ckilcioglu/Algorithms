import math
import random


def quick_sort(a, start, end):
    if start < end:
        q = partition(a, start, end)
        quick_sort(a, start, q-1)
        quick_sort(a, q+1, end)


def partition(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    i += 1
    a[i], a[r] = a[r], a[i]
    return i


if __name__ == "__main__":
    the_list = [random.randint(0, 1000) for i in range(100)]
    print(f"List before sorting:\n{the_list}")
    quick_sort(the_list, start=0, end=len(the_list) - 1)
    print(f"List after sorting:\n{the_list}")
