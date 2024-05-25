# semanage boolean

> Manage persistent SELinux boolean settings.
> See also: `semanage` for managing SELinux policies, `getsebool` for checking boolean values, and `setsebool` for applying non-persistent boolean settings.
> More information: <https://manned.org/man/semanage-boolean>.

- List all booleans settings:

`sudo semanage boolean {{-l|--list}}`

- List all user-defined boolean settings without headings:

`sudo semanage boolean {{-l|--list}} {{-C|--locallist}} {{-n|--noheading}}`

- Set or unset a boolean persistently:

`sudo semanage boolean {{-m|--modify}} {{-1|--on|-0|--off}} {{haproxy_connect_any}}`
