# togglesebool

> Flip the current (non-persistent) values of SELinux booleans.
> Note: This command is deprecated, use `setsebool` instead.
> More information: <https://manned.org/togglesebool>.

- Flip the current (non-persistent) values of the specified booleans:

`sudo togglesebool {{virt_use_samba|virt_use_usb|...}}`

- Flip multiple booleans:

`sudo togglesebool {{key1 key2 ...}}`
