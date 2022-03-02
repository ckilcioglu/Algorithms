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

int insertion_sort(int *a, int a_length)
{
    for (int i = 1; i < a_length; i++)
    {
        int key = a[i];
        int j = i - 1;
        while (j >= 0 && a[j] > key)
        {
            a[j+1] = a[j];
            j -= 1;
        }
        a[j + 1] = key;
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

    int ret = insertion_sort(a, a_size);
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