# setsid

> Run a program in a new session if the calling process is not a process group leader.
> The created session is by default not controlled by the current terminal.
> More information: <https://manned.org/setsid>.

- Run a program in a new session:

`setsid {{program}}`

- Run a program in a new session discarding the resulting output and error:

`setsid {{program}} > /dev/null 2>&1`

- Run a program creating a new process:

`setsid --fork {{program}}`

- Return the exit code of a program as the exit code of setsid when the program exits:

`setsid --wait {{program}}`

- Run a program in a new session setting the current terminal as the controlling terminal:

`setsid --ctty {{program}}`
