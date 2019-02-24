# exec

> Replace the current process with another process.

- Replace with specified command using the current environment variable:

`exec {{command -with -flags}}`

- Replace with specified command using the initialized environment variable:

`exec -c {{command -with -flags}}`

- Replace with specified command and login to the default shell:

`exec -l {{command -with -flags}}`

- Replace with specified command and rename the process name:

`exec -a {{process_name}} {{command -with -flags}}`
