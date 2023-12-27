# exec

> Replace the current process with another process.
> More information: <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#exec>.

- Replace with the specified command using the current environment variables:

`exec {{command -with -flags}}`

- Replace with the specified command, clearing environment variables:

`exec -c {{command -with -flags}}`

- Replace with the specified command and login using the default shell:

`exec -l {{command -with -flags}}`

- Replace with the specified command and change the process name:

`exec -a {{process_name}} {{command -with -flags}}`
