# resolveip

> Resolve hostnames to their IP addresses and vice versa.
> More information: <https://mariadb.com/docs/server/clients-and-utilities/networking-tools/resolveip>.

- Resolve a hostname to an IP address:

`resolveip {{example.org}}`

- Resolve an IP address to a hostname:

`resolveip {{1.1.1.1}}`

- Resolve a hostname to an IP address with less output:

`resolveip {{[-s|--silent]}} {{example.org}}`
