# openrc

> The OpenRC service manager.
> See also: `rc-status`, `rc-update`, `rc-service`.
> More information: <https://wiki.gentoo.org/wiki/OpenRC>.

- Change to a specific runlevel:

`sudo openrc {{runlevel_name}}`

- Change to a specific runlevel, but don't stop any existing services:

`sudo openrc {{[-n|--no-stop]}} {{runlevel_name}}`
