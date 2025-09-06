# logrotate

> Rotates, compresses, and mails system logs.
> More information: <https://manned.org/logrotate>.

- Trigger a run manually:

`logrotate {{path/to/logrotate.conf}} --force`

- Run using a specific command to mail reports:

`logrotate {{path/to/logrotate.conf}} --mail {{/usr/bin/mail_command}}`

- Run without using a state (lock) file:

`logrotate {{path/to/logrotate.conf}} --state /dev/null`

- Run and skip the state (lock) file check:

`logrotate {{path/to/logrotate.conf}} --skip-state-lock`

- Tell `logrotate` to log verbose output into the log file:

`logrotate {{path/to/logrotate.conf}} --log {{path/to/log_file}}`
