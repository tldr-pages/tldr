# runcon

> Run a program in a different SELinux security context.
> With neither context nor command, print the current security context.
> More information: <https://www.gnu.org/software/coreutils/runcon>.

- Determine the current domain:

`runcon`

- Specify the domain to run a command in:

`runcon -t {{domain}}_t {{command}}`

- Specify the context role to run a command with:

`runcon -r {{role}}_r {{command}}`

- Specify the full context to run a command with:

`runcon {{user}}_u:{{role}}_r:{{domain}}_t {{command}}`
