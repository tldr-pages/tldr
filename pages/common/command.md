# command

> Command forces the shell to execute the program and ignore any functions, builtins and aliases with the same name.

- Execute the ls program literally, even if an ls alias exists:

`command {{ls}}`

- Display the path to the executable or the alias definition of a specific command:

`command -v {{command_name}}`
