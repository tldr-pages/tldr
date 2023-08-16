# kinit

> Authenticate a principal with a Kerberos server to gain and cache a ticket.
> Note: A Kerberos principal can be either a user, service, or application.
> More information: <https://web.mit.edu/kerberos/krb5-1.12/doc/user/user_commands/kinit.html>.

- Authenticate a user and obtain a ticket-granting ticket:

`kinit {{username}}`

- Renew a ticket-granting ticket:

`kinit -R`

- Specify a lifetime for the ticket:

`kinit -l {{5h}}`

- Specify a total renewable lifetime for the ticket:

`kinit -r {{1w}}`

- Specify a different principal name to authenticate as:

`kinit -p {{principal@REALM}}`

- Specify a different keytab file to authenticate with:

`kinit -t {{path/to/keytab}}`
