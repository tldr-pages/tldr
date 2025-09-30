# logger

> Add messages to the system log.
> More information: <https://manned.org/logger>.

- Log a message to syslog:

`logger {{message}}`

- Take input from `stdin` and log to syslog:

`echo {{log_entry}} | logger`

- Send the output to a remote syslog server running at a given port. Default port is 514:

`echo {{log_entry}} | logger {{[-n|--server]}} {{hostname}} {{[-P|--port]}} {{port}}`

- Use a specific tag for every line logged. Default is the name of logged in user:

`echo {{log_entry}} | logger {{[-t|--tag]}} {{tag}}`

- Log messages with a given priority. Default is `user.notice`. See `man logger` for all priority options:

`echo {{log_entry}} | logger {{[-p|--priority]}} {{user.warning}}`
