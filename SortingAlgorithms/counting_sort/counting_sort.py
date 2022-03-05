import random


def counting_sort(a, k):
    c = [0] * k
    b = list(a)
    for i in range(len(a)):
        c[a[i]] += 1
    for i in range(1, len(c)):
        c[i] += c[i-1]
    for i in reversed(range(len(a))):
        b[c[a[i]] - 1] = a[i]
        c[a[i]] -= 1
    return b


if __name__ == "__main__":
    the_list = [random.randint(0, 99) for i in range(100)]
    print(f"List before sorting:\n{the_list}")
    sorted_list = counting_sort(the_list, 100)
    print(f"List after sorting:\n{sorted_list}")
