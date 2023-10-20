#include <stdio.h>

// Write a program to print n elements of an array
int main()
{
    int sum = 0, num_ele, find_ele;
    printf("Enter number of elements in the array : ");
    scanf("%d", &num_ele);
    
    int test[num_ele];
    // Loop to enter values into the array;
    for (int i = 0; i < sizeof(test) / sizeof(test[0]); i++)
    {
        printf("Enter an elemnt at the %d index in the array : ", i);
        scanf("%d", &test[i]);
    }
    
    // Loop to print the elements of the array;
    for (int j = 0; j < sizeof(test) / sizeof(test[0]); j++)
    {
        printf("\nElement at %d index is %d\n", j, test[j]);
    }

    // Loop to add all elements of the array 
    for (int m = 0; m < sizeof(test) / sizeof(test[0]); m++)
    {
        sum += test[m];
    }
    printf("\nSum of all the elements in the array is = %d\n", sum);
    
    // Loop to find the smallest number in an array
    for (int a = 0; a < sizeof(test) / sizeof(test[0]); a++)
    {
        int smallest_number = 10000, loop1var;
        if (test[a] < smallest_number)
        {
            smallest_number = test[a];
        }
        printf("\nThe smallest number of the array is = %d\n", smallest_number);
    }
    
    // Loop to find the largest number the array
    for (int b = 0; b < sizeof(test) / sizeof(test[0]); b++)
    {
        int largest_number = 0, loop1var;
        if (test[b] > largest_number)
        {
            largest_number = test[b];
        }
        printf("\nThe smallest number of the array is = %d\n", largest_number);    
    }
    
    // Loop to find a particular element in the array
    printf("\nEnter the element to be found : ");
    scanf("%d", &find_ele);
        
    for (int c = 0; c < sizeof(test) / sizeof(test[0]); c++)
    {
        if (find_ele == test[c])
        {
            printf("\nElement found at index %d\n", c);
            break;
        }
        else
        {
            printf("\nElement not found in the array.\n");
            break;
        }
        
    }
    return 0;
}
