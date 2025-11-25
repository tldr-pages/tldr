# systemctl service-log-level

> Get or set the runtime log level of a service via D-Bus.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#service-log-level%20SERVICE%20%5BLEVEL%5D>.

- Show the current log level of a service:

`systemctl service-log-level {{service_name}}`

- Set the log level of a service (the level name can be replaced with a number from 0 to 7):

`systemctl service-log-level {{service_name}} {{emerg|alert|crit|err|warning|notice|info|debug}}`
