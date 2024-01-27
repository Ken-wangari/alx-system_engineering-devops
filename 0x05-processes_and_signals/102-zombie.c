#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * main - Creates five zombie processes.
 *
 * Return: Always 0.
 */
int main(void)
{
    pid_t pid;
    int count;

    for (count = 0; count < 5; count++)
    {
        pid = fork();
        if (pid < 0)
        {
            perror("fork failed");
            exit(EXIT_FAILURE);
        }
        else if (pid == 0)
        {
            // Child process
            printf("Zombie process created, PID: %d\n", getpid());
            exit(EXIT_SUCCESS);
        }
        // Parent process continues to fork
    }

    // Parent process continues running an infinite loop
    while (1)
    {
        sleep(1);
    }

    return (EXIT_SUCCESS);
}

