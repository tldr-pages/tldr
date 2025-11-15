# audit2why

> Explain SELinux denials from audit logs.
> Part of the `policycoreutils-python-utils` package.
> See also: `audit2allow`, `ausearch`, `sealert`.
> More information: <https://manned.org/audit2why>.

- Explain the most recent SELinux denial:

`sudo audit2why`

- Explain SELinux denials from a specific audit log file:

`sudo audit2why {{[-i|--input]}} {{path/to/audit.log}}`

- Explain all SELinux denials from the audit log:

`sudo ausearch {{[-m|--message]}} avc | audit2why`

- Explain denials for a specific service:

`sudo ausearch {{[-m|--message]}} avc {{[-c|--comm]}} {{service_name}} | audit2why`
