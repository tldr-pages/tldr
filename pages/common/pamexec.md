# pamexec

> Execute a shell command on each image in a Netpbm file.
> See also: `pamfile`, `pampick`, `pamsplit`.
> More information: <https://netpbm.sourceforge.net/doc/pamexec.html>.

- Execute a shell command on each image in a Netpbm file:

`pamexec {{command}} {{path/to/image.pam}}`

- Stop processing if a command terminates with a nonzero exit status:

`pamexec {{command}} {{path/to/image.pam}} -check`
