# runcon

> Run a program in a different SELinux security context.
> With neither CONTEXT nor COMMAND, print the current security context.

- Determine the current domain:

`runcon`

- Specify the domain to run a command in:

`runcon -t CONTEXT-TYPE_t {{command}}`

- Specify the role type to run a command with:

`runcon -r ROLE_TYPE_r {{command}}`

- Specify the full context to run a command with:

`runcon USER_TYPE_u:ROLE_TYPE_r:CONTEXT_TYPE_t {{command}}`
