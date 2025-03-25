# avahi-resolve

> Translate between host names and IP Addresses.
> More information: <https://www.avahi.org/>.

- Resolve a local service to its IPv4:

`avahi-resolve -4 {{[-n|--name]}} {{service.local}}`

- Resolve an IP to a hostname, verbosely:

`avahi-resolve {{[-v|--verbose]}} {{[-a|--address]}} {{IP}}`
