# systemctl service-log-target

> Get or set the log target for a service.
> Only works for D-Bus integrated services.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#service-log-target%20SERVICE%20[TARGET]>.

- Show the current log target for a service:

`systemctl service-log-target {{service_name}}`

- Set the log target to `console` (send logs to `stderr`):

`systemctl service-log-target {{service_name}} console`

- Set the log target to `journal` (send logs to `systemd-journald`):

`systemctl service-log-target {{service_name}} journal`

- Set the log target to `syslog` (send logs to `/dev/log`):

`systemctl service-log-target {{service_name}} syslog`

- Allow systemd to choose an appropriate log target:

`systemctl service-log-target {{service_name}} auto`

- Disable all log output:

`systemctl service-log-target {{service_name}} null`
