# command

> Command forces the shell to execute the program and ignore any functions, builtins and aliases with the same name.

- Execute the ls program literally, even if an ls alias exists:

`command {{ls}}`

- Find the path to the executable of the command ls:

`command -v {{ls}}`
