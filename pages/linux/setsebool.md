# setsebool

> Set SELinux boolean value.
> See also: `semanage-boolean`, `getsebool`.
> More information: <https://manned.org/setsebool>.

- Show the current setting of [a]ll booleans:

`getsebool -a`

- Set or unset a boolean temporarily (non-persistent across reboot):

`sudo setsebool {{httpd_can_network_connect}} {{1|true|on|0|false|off}}`

- Set or unset a boolean [P]ersistently:

`sudo setsebool -P {{container_use_devices}} {{1|true|on|0|false|off}}`

- Set or unset multiple booleans at once [P]ersistently:

`sudo setsebool -P {{key1 1 key2 0 ...}}`

- Set or unset a boolean persistently (alternative method using `semanage-boolean`):

`sudo semanage boolean {{[-m|--modify]}} {{-1|--on|-0|--off}} {{haproxy_connect_any}}`
