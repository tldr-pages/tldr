# avahi-resolve

> Translate between host names and IP Addresses.
> More information: <https://www.avahi.org/>.

- Resolve a local service to its IPv4:

`avahi-resolve -4 --name {{service.local}}`

- Resolve an IP to a host name, verbosely:

`avahi-resolve --verbose --address {{IP}}`
