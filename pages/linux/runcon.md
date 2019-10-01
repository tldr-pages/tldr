0# runcon

> Run a program in a different SELinux security context.
> With neither CONTEXT nor COMMAND, print the current security context.

- Determine current domain:

`runcon`

- Specify the domain that you want to run a program or script in:

`runcon -t CONTEXT-TYPE_t {{command}}` 

- Specify the role type that you want to run a program or script with:

`runcon -r ROLE_TYPE_r {{command}}` 

- Specify the full context to run a program or script with:

`runcon USER_TYPE_u:ROLE_TYPE_r:CONTEXT_TYPE_t {{command}}
