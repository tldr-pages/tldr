# exec

> Replace the current process with another process.

- Replace with the specified command using the current environment variables:

`exec {{command -with -flags}}`

- Replace with the specified command using initialized environment variables:

`exec -c {{command -with -flags}}`

- Replace with the specified command and login to the default shell:

`exec -l {{command -with -flags}}`

- Replace with the specified command and rename the process name:

`exec -a {{process_name}} {{command -with -flags}}`
