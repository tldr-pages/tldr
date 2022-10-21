# logrotate

> Rotates, compresses, and mails system logs.
> More information: <https://manned.org/logrotate.8>.

- Trigger a run of logrotate manually:

`logrotate {{path/to/logrotate.conf}} --force`

- Run logrotate using a specific mail_binary to send reports:

`logrotate {{path/to/logrotate.conf}} --mail {{/usr/bin/mail_binary}}`

- Run without using a state (lock) file:

`logrotate {{path/to/logrotate.conf}} --state /dev/null`

- Run logrotate and skip the state (lock) file check:

`logrotate {{path/to/logrotate.conf}} --skip-state-lock`

- Tell logrotate to log verbose output into the log_file:

`logrotate {{path/to/logrotate.conf}} --log {{path/to/log_file}}`
