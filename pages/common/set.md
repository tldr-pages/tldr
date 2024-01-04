# set

> Display, set or unset values of shell attributes and positional parameters.
> More information: <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#set>.

- Display the names and values of shell variables:

`set`

- Mark variables that are modified or created for export:

`set -a`

- Notify of job termination immediately:

`set -b`

- Set various options, e.g. enable `vi` style line editing:

`set -o {{vi}}`

- Set the shell to exit as soon as the first error is encountered (mostly used in scripts):

`set -e`
