import sys
import random


def parent(index):
    return (index - 1) // 2


def left_child(index):
    return index * 2 + 1


def right_child(index):
    return (index + 1) * 2


def max_heapify(a, index, heap_size):
    largest = index
    left = left_child(index)
    right = right_child(index)

    if left < heap_size and a[left] > a[largest]:
        largest = left

    if right < heap_size and a[right] > a[largest]:
        largest = right

    if largest != index:
        a[largest], a[index] = a[index], a[largest]
        max_heapify(a, largest, heap_size)


def build_max_heap(a):
    for i in reversed(range(len(a) // 2)):
        max_heapify(a, i, len(a))


def heap_sort(a):
    build_max_heap(a)
    heap_size = len(a)
    for i in reversed(range(1, len(a))):
        a[0], a[i] = a[i], a[0]
        heap_size -= 1
        max_heapify(a, 0, heap_size)


if __name__ == "__main__":
    the_list = [random.randint(0, 1000) for i in range(100)]
    print(f"List before sorting:\n{the_list}")
    heap_sort(the_list)
    print(f"List after sorting:\n{the_list}")
