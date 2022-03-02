#include <stdio.h>
#include <stdlib.h>
#include <time.h>


void print_the_array(int *a, int a_length)
{
    if (a_length > 0)
    {
        printf("[");
        for (int i = 0; i < a_length-1; i++)
        {
            printf(" %i,", a[i]);
        }
        printf(" %i ]\n", a[a_length - 1]);
    }
}

int parent(int index)
{
    return (index - 1) >> 1;
}

int left_child(int index)
{
    return (index << 1) + 1;
}

int right_child(int index)
{
    return (index << 1) + 2;
}

void max_heapify(int *a, int heap_size, int index)
{
    int left = left_child(index);
    int right = right_child(index);
    int largest = index;

    if (left < heap_size && a[left] > a[largest])
    {
        largest = left;
    }
    if (right < heap_size && a[right] > a[largest])
    {
        largest = right;
    }
    if (largest != index)
    {
        int tmp = a[index];
        a[index] = a[largest];
        a[largest] = tmp;
        max_heapify(a, heap_size, largest);
    }
}

void build_max_heap(int *a, int a_length)
{
    for (int i = (a_length >> 1) - 1; i >= 0; i--)
    {
        max_heapify(a, a_length, i);
    }
}


int heap_sort(int *a, int a_length)
{
    build_max_heap(a, a_length);
    int heap_size = a_length;
    for (int i = a_length-1; i > 0; i--)
    {
        int tmp = a[i];
        a[i] = a[0];
        a[0] = tmp;
        heap_size -= 1;
        max_heapify(a, heap_size, 0);
    }
    return 0;
}


int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("You should enter the length of list\n");
        return 1;
    }
    int a_size = atoi(argv[1]);
    if (a_size <= 0)
    {
        printf("Length of list should be a positive number\n");
        return 1;
    }
    
    int *a = malloc(a_size * sizeof(int));
    srand(time(NULL));
    for (int i = 0; i < a_size; i++)
    {
        int num = (rand() % 1000) + 1;
        a[i] = num;
    }

    printf("Before sorting\n");
    print_the_array(a, a_size);

    int ret = heap_sort(a, a_size);
    if (ret != 0)
    {
        printf("Sorting did not work as expected\n");
        free(a);
        return 1;
    }

    printf("After sorting\n");
    print_the_array(a, a_size);
    
    free(a);
    return 0;
}