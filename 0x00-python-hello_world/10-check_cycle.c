#include"lists.h"

/**
 * check_cycle - checks if there is a cycle in a linked list
 *
 * @list: pointer to head of the list to checked
 *
 * Return: 1 if there is a list and 0 if there isn't
 */
int check_cycle(listint_t *list)
{
	listint_t *curr_1, *curr_2;

	curr_1 = curr_2 = list;

	if ((list == NULL) || (list->next))
		return (0);

	while (1)
	{
		curr_1 = curr_1->next;
		curr_2 = (curr_2->next)->next;

		if (curr_1 == curr_2)
			return (1);
		if ((curr_1 == NULL) || (curr_2 == NULL))
			return (0);
	}
}
