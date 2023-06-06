#include "lists.h"

/**
 * check_cycle - linked list cycle checker
 * @list: linked list to be checked
 *
 * Return: 1 if it's true, 0 if it's false
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
