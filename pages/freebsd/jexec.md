# jexec

> Execute a command inside an existing FreeBSD jail.
> See also: `jls`, `jail`.
> More information: <https://man.freebsd.org/cgi/man.cgi?jexec>.

- Open a shell in a jail by name:

`jexec {{jail_name}}`

- Open a shell in a jail by JID:

`jexec {{jail_id}}`

- Run a command in a jail:

`jexec {{jail_name}} {{command}}`

- Open a shell in a jail with a clean environment:

`jexec -l {{jail_name}} sh`

- Run as a user from the host environment:

`jexec -u {{username}} {{jail_name}}`

- Run as a user from inside the jail:

`jexec -U {{username}} {{jail_name}}`

- Run a command from a specific working directory inside the jail:

`jexec -d {{path/to/directory}} {{jail_name}} {{command}}`

- Open a login shell as root inside the jail:

`jexec -l {{jail_name}} login -f root`
