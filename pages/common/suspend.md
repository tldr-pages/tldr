# suspend

> Suspend the execution of the current shell.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#index-suspend>.

- Suspend the current shell (useful for when you are in nested shells like `su`):

`{{bash}} <Enter> suspend`

- Continue from suspension if `suspend` was used in a non-nested shell (run this in a separate terminal):

`pkill -CONT bash`

- Force suspension even if this would lock you out of the system:

`suspend -f`
