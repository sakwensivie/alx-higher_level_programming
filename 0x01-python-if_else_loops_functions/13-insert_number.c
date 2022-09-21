#include"lists.h"

/**
 * insert_node - inserts an element into a sorted linked list
 *
 * @head: pointer to the head of the list
 * @number: number to be inserted
 *
 * Return: the linked list
 */

listint_t *insert_node(listint_t **head, int number);
{
	listint_t *new, *first, *second;

	if (*head == NULL)
		return (NULL);

	first = *head;
	second = (*head)->next;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		printf("memory allocation failed");
		exit(98);
	}

	new->n = number;

	while (second)
	{
		first = first->next;
		second = second->next;

		if ((first->n <= number) && (second >= number))
			break;
	}

	first->next = new;
	new->next = second;

	return (*head);
}
