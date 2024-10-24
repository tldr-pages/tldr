# sv

> Control a running runsv service.
> More information: <https://manned.org/sv.8>.

- Start a service:

`sudo sv up {{path/to/service}}`

- Stop a service:

`sudo sv down {{path/to/service}}`

- Get service status:

`sudo sv status {{path/to/service}}`

- Reload a service:

`sudo sv reload {{path/to/service}}`

- Start a service, but only if it's not running and don't restart it if it stops:

`sudo sv once {{path/to/service}}`
