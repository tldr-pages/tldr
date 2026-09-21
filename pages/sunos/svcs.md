# svcs

> List information about running services.
> More information: <https://www.unix.com/man-page/sunos/1/svcs>.

- List all running services:

`svcs`

- List services that are not running:

`svcs -vx`

- List information about a service:

`svcs {{service}}`

- Show location of service log file:

`svcs -L {{service}}`

- Display end of a service log file:

`tail $(svcs -L {{service}})`
