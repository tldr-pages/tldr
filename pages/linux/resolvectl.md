# resolvectl

> Resolve domain names, IPV4 and IPv6 addresses, DNS resource records, and services.
> Introspect and reconfigure the DNS resolver.
> More information: <https://www.freedesktop.org/software/systemd/man/resolvectl.html>.

- Show DNS settings:

`resolvectl status`

- Resolve the IPv4 and IPv6 addresses for one or more domains:

`resolvectl query {{domain}}`

- Retrieve the domain of a specified IP:

`resolvectl query {{IP}}`

- Retrieve an MX record of {{domain}}:

`resolvectl  --legend=no -t MX query  {{domain}}`

- Resolve an SRV record, for example _xmpp-server._tcp gmail.com:

`resolvectl service _{{service}}._{{protocol}} {{name}}`

- Retrieve the public key from an email address with an OPENPGP Record:

`resolvectl opengpg {{email}}`

- Retreive a TLS key:

`resolvectl tlsa tcp {{domain}}:443`
