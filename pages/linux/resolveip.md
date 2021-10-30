# resolveip

> Resolve hostnames to their IP addresses and vice versa.
> More information: <https://mariadb.com/kb/en/resolveip/>.

- Resolve a hostname to an IP address:

`resolveip {{example.org}}`

- Resolve an IP address to a hostname:

`resolveip {{1.1.1.1}}`

- Silent mode. Produces less output:

`resolveip --silent {{example.org}}`
