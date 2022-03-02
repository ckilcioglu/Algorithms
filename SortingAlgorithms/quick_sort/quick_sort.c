#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
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

int partition(int *a, int p, int r)
{
    int x = a[r];
    int i = p - 1;

    for (int j = p; j < r; j++)
    {
        if (a[j] <= x)
        {
            i += 1;
            int tmp = a[i];
            a[i] = a[j];
            a[j] = tmp;
        }
    } 
    i += 1;
    a[r] = a[i];
    a[i] = x;
    return i;
}

int quick_sort(int *a, int start, int end)
{
    if (start < end)
    {
        int q = partition(a, start, end);
        quick_sort(a, start, q - 1);
        quick_sort(a, q + 1, end);
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

    int ret = quick_sort(a, 0, a_size - 1);
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