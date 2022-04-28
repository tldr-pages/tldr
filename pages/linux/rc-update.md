# rc-update

> Add and remove OpenRC services to and from runlevels.
> See also `openrc`.
> More information: <https://manned.org/rc-update>.

- List all services and the runlevels they are added to:

`rc-update show`

- Add a service to a runlevel:

`sudo rc-update add {{service_name}} {{runlevel}}`

- Delete a service from a runlevel:

`sudo rc-update delete {{service_name}} {{runlevel}}`

- Delete a service from all runlevels:

`sudo rc-update --all delete {{service_name}}`
