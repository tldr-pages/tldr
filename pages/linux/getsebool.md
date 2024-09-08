# getsebool

> Get SELinux boolean value.
> See also: `semanage-boolean`, `setsebool`.
> More information: <https://manned.org/man/getsebool>.

- Show the current setting of a boolean:

`getsebool {{httpd_can_connect_ftp}}`

- Show the current setting of [a]ll booleans:

`getsebool -a`

- Show the current setting of all booleans with explanations:

`sudo semanage boolean {{-l|--list}}`
