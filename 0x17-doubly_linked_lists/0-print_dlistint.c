#include <stdio.h>
#include "lists.h"
/**
 * print_dlistint - print all the element in te dlistint
 * @h: this is a pointer
 * Return: number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t iterate = 0;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		h = h->next;
		iterate++;
	}
	return (iterate);
}
