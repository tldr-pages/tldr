# journalctl

> Query the systemd journal.

- Show all messages from this boot:

`journalctl -b`

- Show all messages from last boot:

`journalctl -b -1`

- Follow new messages (like `tail -f` for traditional syslog):

`journalctl -f`

- Show all messages by a specific unit:

`journalctl -u {{unit}}`

- Show all messages by a specific process:

`journalctl _PID={{pid}}`

- Show all messages by a specific executable:

`journalctl {{path/to/executable}}`
