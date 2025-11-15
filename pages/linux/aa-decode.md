# aa-decode

> Decode AppArmor audit logs into a human-readable format.
> More information: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-decode.8>.

- Decode a hex string:

`aa-decode {{hexstring}}`

- Decode a log file:

`sudo aa-decode {{logfile}}`

- Decode logs from `stdin` (e.g., redirected file):

`sudo aa-decode - < {{logfile}}`

- Display help:

`aa-decode {{[-h|--help]}}`
