# lvmpolld

> LVM poll daemon that supervises long-running LVM operations.
> More information: <https://manned.org/lvmpolld>.

- Start the daemon in the foreground:

`lvmpolld {{[-f|--foreground]}}`

- Start in the foreground with debug logging:

`lvmpolld {{[-f|--foreground]}} {{[-l|--log]}} debug`

- Set the idle shutdown timeout (seconds):

`lvmpolld {{[-t|--timeout]}} {{300}}`

- Use a custom socket path:

`lvmpolld {{[-s|--socket]}} {{/tmp/lvmpolld.socket}}`

- Use a custom PID file:

`lvmpolld {{[-p|--pidfile]}} {{/tmp/lvmpolld.pid}}`

- Dump the current state:

`lvmpolld --dump`
