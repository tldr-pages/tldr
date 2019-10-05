# lastcomm

> Show last commands executed (from acct - GNU Accounting utilities).
> More information: <https://manpages.debian.org/stable/acct/lastcomm.1.en.html>.


- Print informations about all of the commands in the acct (record file):

`lastcomm`

- Display commands executed by {{user}}:

`lastcomm --user {{user}}`

- Display informations about {{command}} executed on the system:

`lastcomm --command {{command}}`

- Display informations about {{terminal_name}} activities executed on the system:

`lastcomm --tty {{terminal_name}}`
