import sys
import random


def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key


if __name__ == "__main__":
    the_list = [random.randint(0, 1000) for i in range(100)]
    print(f"List before sorting:\n{the_list}")
    insertion_sort(the_list)
    print(f"List after sorting:\n{the_list}")
