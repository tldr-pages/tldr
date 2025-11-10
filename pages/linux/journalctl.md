# journalctl

> Query the systemd journal.
> See also: `dmesg`.
> More information: <https://www.freedesktop.org/software/systemd/man/journalctl.html>.

- Show all messages with priority level 3 (errors) from this boot:

`journalctl {{[-b|--boot]}} {{[-p|--priority]}} 3`

- Delete journal logs which are older than 2 days:

`journalctl --vacuum-time 2d`

- Show only the last `n` lines and follow new messages (like `tail -f` for traditional syslog):

`journalctl {{[-n|--lines]}} {{n}} {{[-f|--follow]}}`

- Show all messages by a specific unit:

`journalctl {{[-u|--unit]}} {{unit}}`

- Show logs for a given unit since the last time it started:

`journalctl _SYSTEMD_INVOCATION_ID=$(systemctl show --value --property=InvocationID {{unit}})`

- Filter messages within a time range (either timestamp or placeholders like "yesterday"):

`journalctl {{[-S|--since]}} {{now|today|yesterday|tomorrow}} {{[-U|--until]}} "{{YYYY-MM-DD HH:MM:SS}}"`

- Show all messages by a specific process:

`journalctl _PID={{pid}}`

- Show all messages by a specific executable:

`journalctl {{path/to/executable}}`
