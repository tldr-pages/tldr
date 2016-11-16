# logger

> Add messages to syslog.

- Log a message to syslog:

`logger {{message}}`

- Take input from stdin and log to syslog:

`tail -f {{app.log}} | logger`

- Send the output to a remote syslog server running at a given port. Default port is `syslog`:

`tail -f {{app.log}} | logger -h {{hostname}} -P {{port}}`

- Use a specific tag for every line logged. Default is the name of logged in user:

`tail -f {{app.log}} | logger -t {{tag}}`

- Log messages with a given priority. Default is `user.notice`. See `man logger` for all priority options:

`tail -f {{app.log}} | logger -p {{user.warning}}`
