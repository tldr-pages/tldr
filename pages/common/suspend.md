# suspend

> Suspend the execution of the current shell.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#index-suspend>.

- Suspend the current shell (useful for when you are in nested shells like `su`):

`{{bash}} <Enter> suspend`

- Run in a separate terminal to continue from suspension if `suspend` was used in a non-nested shell:

`pkill -CONT bash`

- Force suspension even if this would lock you out of the system:

`suspend -f`
