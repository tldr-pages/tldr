# command

> Command forces the shell to execute the program and ignore any functions, builtins and aliases with the same name.
> More information: <https://manned.org/command>.

- Execute the `ls` program literally, even if an `ls` alias exists:

`command {{ls}}`

- Find and execute a command using a default `$PATH` (`/bin:/usr/bin:/sbin:/usr/sbin:/etc:/usr/etc`) that guarantees to find all standard utilities:

`command -p {{command_name}}`

- Display the path to the executable or the alias definition of a specific command:

`command -v {{command_name}}`
