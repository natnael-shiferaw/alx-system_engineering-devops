#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>

/**
 * infinite_while - This Function is used to run
 * a loop specifically an infinite while loop.
 *
 * Return: It always returns 0.
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - This main function is used to create
 *  5 zombie processes.
 *
 * Return: It always returns 0.
 */

int main(void)
{
char zombie_count = 0;
pid_t Pid;

while (zombie_count < 5)
{
Pid = fork();

if (Pid > 0)
{
	printf("Zombie process created, PID: %d\n", Pid);
	sleep(1);
	zombie_count++;
}
else
	exit(0);
}

infinite_while();

return (EXIT_SUCCESS);
}
