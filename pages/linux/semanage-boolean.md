# semanage boolean

> Manage persistent SELinux boolean settings.
> See also: `semanage`, `getsebool`, `setsebool`.
> More information: <https://manned.org/man/semanage-boolean>.

- List all booleans settings:

`sudo semanage boolean {{-l|--list}}`

- List all user-defined boolean settings without headings:

`sudo semanage boolean {{-l|--list}} {{-C|--locallist}} {{-n|--noheading}}`

- Set or unset a boolean temporarily (non-persistent across reboot):

`sudo setsebool {{httpd_can_network_connect}} {{1|true|on|0|false|off}}`

- Set or unset a boolean persistently:

`sudo semanage boolean {{-m|--modify}} {{-1|--on|-0|--off}} {{haproxy_connect_any}}`
