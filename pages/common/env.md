# env

> Show the environment or run a program in a modified environment.

- Show the environment:

`env`

- Run a program. Often used in scripts after the shebang (#!) for looking up the path to the program:

`env {{program}}`

- Clear the environment and run a program:

`env -i {{program}}`

- Remove variable from the environment and run a program:

`env -u {{variable}} {{program}}`

- Set a variable and run a program:

`env {{variable}}={{value}} {{program}}`
