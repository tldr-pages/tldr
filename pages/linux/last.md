# last

> List information of last user logins.
> See also: `lastb`, `login`.
> More information: <https://manned.org/last.1>.

- List login information (e.g., username, terminal, boot time, kernel) of all users:

`last`

- List login information of a specific user:

`last {{username}}`

- List information of a specific TTY:

`last {{tty1}}`

- List most recent information (by default, the newest are at the top):

`last | tac`

- List information of system boots:

`last "{{system boot}}"`

- List information with a specific [t]imestamp format:

`last --time-format {{notime|full|iso}}`

- List information [s]ince a specific time and date:

`last --since {{-7days}}`

- List information (i.e., hostname and IP) of remote hosts:

`last --dns`
