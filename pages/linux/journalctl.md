# journalctl

> Query the systemd journal.
> More information: <https://manned.org/journalctl>.

- Show all messages with priority level 3 (errors) from this [b]oot:

`journalctl -b --priority={{3}}`

- Delete journal logs which are older than 2 days:

`journalctl --vacuum-time={{2d}}`

- [f]ollow new messages (like `tail -f` for traditional syslog):

`journalctl -f`

- Show all messages by a specific [u]nit:

`journalctl -u {{unit}}`

- Show logs for a given unit since the last time it started:

`journalctl _SYSTEMD_INVOCATION_ID=$(systemctl show --value --property=InvocationID {{unit}})`

- Filter messages within a time range (either timestamp or placeholders like "yesterday"):

`journalctl --since {{now|today|yesterday|tomorrow}} --until {{YYYY-MM-DD HH:MM:SS}}`

- Show all messages by a specific process:

`journalctl _PID={{pid}}`

- Show all messages by a specific executable:

`journalctl {{path/to/executable}}`
