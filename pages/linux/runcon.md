# runcon

> Run a program in a different SELinux security context.
> See also: `secon`.
> More information: <https://www.gnu.org/software/coreutils/runcon>.

- Print the security context of the current execution context:

`runcon`

- Specify the domain to run a command in:

`runcon -t {{domain}}_t {{command}}`

- Specify the context role to run a command with:

`runcon -r {{role}}_r {{command}}`

- Specify the full context to run a command with:

`runcon {{user}}_u:{{role}}_r:{{domain}}_t {{command}}`
