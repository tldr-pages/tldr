# logrotate

> Rotates, compresses, and mails system logs.
> More information: <https://manned.org/logrotate.8>

- Force logrotate to run outside of normal interval:

`logrotate {{path/to/logrotate.conf}} --force`

- Set mail binary for logrotate to Mutt:

`logrotate {{path/to/logrotate.conf}} --mail /usr/bin/mutt`

- Run logrotate without lock or state file:

`logrotate {{path/to/logrotate.conf}} --state /dev/null`

- Skip lock file check:

`logrotate {{path/to/logrotate.conf}} --skip-state-lock`

- Log instances of logrotate:

`logrotate {{path/to/logrotate.conf}} --log {{path/to/log/file}}`
