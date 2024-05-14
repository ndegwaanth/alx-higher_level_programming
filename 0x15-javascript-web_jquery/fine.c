#include <stdio.h>


void main()
{
    int i;
    
    i = 10; 
    while (i < 20)
    {
        printf("%d", i % 2);
        i++;
    }
}