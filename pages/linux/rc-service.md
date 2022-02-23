# rc-service

> Locate and run OpenRC services with arguments.
> See also `openrc`.
> More information: <https://manned.org/rc-service>.

- Show a service's status:

`rc-service {{service_name}} status`

- Start a service:

`sudo rc-service {{service_name}} start`

- Stop a service:

`sudo rc-servie {{service_name}} stop`

- Restart a service:

`sudo rc-service {{service_name}} restart`

- Simulate running a service's custom command:

`sudo rc-service --dry-run {{service_name}} {{command_name}}`

- Actually run a service's custom command:

`sudo rc-service {{service_name}} {{command_name}}`

- Resolve the location of a service definition on disk:

`sudo rc-service --resolve {{service_name}}`
