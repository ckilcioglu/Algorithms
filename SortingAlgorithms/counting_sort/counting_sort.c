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

int counting_sort(int *a, int a_length, int *b, int k)
{
    int *c = malloc(k * sizeof(int));
    for (int i = 0; i < k; i++)
    {
        c[i] = 0;
    }
    for (int i = 0; i < a_length; i++)
    {
        c[a[i]] += 1;
    }
    for (int i = 1; i < k; i++)
    {
        c[i] += c[i - 1];
    }
    for (int i = a_length - 1; i >= 0; i--)
    {
        b[c[a[i]] - 1] = a[i];
        c[a[i]] -= 1;
    }
    free(c);
    return 0;
}


int main(int argc, char *argv[])
{
    int k = 10;
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
    int *b = malloc(a_size * sizeof(int));
    if (a == NULL || b == NULL)
    {
        printf("Memory allocation problem\n");
        return 1;
    } 
    srand(time(NULL));
    for (int i = 0; i < a_size; i++)
    {
        int num = rand() % k;
        a[i] = num;
    }

    printf("Before sorting\n");
    print_the_array(a, a_size);

    int ret = counting_sort(a, a_size, b, k);
    if (ret != 0)
    {
        printf("Sorting did not work as expected\n");
        free(a);
        free(b);
        return 1;
    }

    printf("After sorting\n");
    print_the_array(b, a_size);
    
    free(a);
    free(b);
    return 0;
}