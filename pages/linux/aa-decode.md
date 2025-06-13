# aa-decode

> Decode AppArmor audit logs into a human-readable format.
> More information: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-decode.8>.

- Decode an audit log file:

`sudo aa-decode {{logfile}}`

- Decode a log file with verbose output:

`sudo aa-decode --verbose {{logfile}}`

- Decode logs from standard input:

`sudo aa-decode - < {{logfile}}`

- Display help information:

`aa-decode --help`
