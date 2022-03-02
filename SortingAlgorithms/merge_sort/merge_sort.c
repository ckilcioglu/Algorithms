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

int merge(int *a, int p, int q, int r)
{
    int n1 = q - p + 1;
    int n2 = r - q;

    int *left = malloc((n1 + 1) * sizeof(int));
    int *right = malloc((n2 + 1) * sizeof(int));

    for (int i = 0; i < n1; i++)
    {
        left[i] = a[p + i];
    }
    left[n1] = INT_MAX;

    for (int i = 0; i < n2; i++)
    {
        right[i] = a[q + i + 1];
    }
    right[n2] = INT_MAX;

    int i = 0, j = 0;

    for (int k = p; k <= r; k++)
    {
        if (left[i] < right[j])
        {
            a[k] = left[i];
            i += 1;
        }
        else
        {
            a[k] = right[j];
            j += 1;
        }
    }

    free(left);
    free(right);
    return 0;
}

int merge_sort(int *a, int start, int end)
{
    if (start < end)
    {
        int q = (start + end) / 2;
        merge_sort(a, start, q);
        merge_sort(a, q+1, end);
        merge(a, start, q, end);
        return 0;
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

    int ret = merge_sort(a, 0, a_size - 1);
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