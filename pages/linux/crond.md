# crond

> Daemon to execute scheduled commands from crontab files.
> More information: <https://manned.org/crond>.

- Start daemon in the background and check for scheduled commands:

`crond`

- Start daemon in the foreground and check for scheduled commands:

`crond -n`

- Send job output from the daemon to the [s]ystem log:

`crond -s`

- Override default limitations and accept custom crontables:

`crond -p`

- Inherit crontab file path from environment settings:

`crond -P`
