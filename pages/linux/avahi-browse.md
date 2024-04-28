# avahi-browse

> Display services and hosts exposed on the local network via mDNS/DNS-SD.
> Avahi is compatible with Bonjour (Zeroconf) found in Apple devices.
> More information: <https://www.avahi.org/>.

- List services available on the local network along with their addresses and ports, ignoring ones on the local machine:

`avahi-browse --all --resolve --ignore-local`

- Quickly list services in the local network in SSV format for scripts:

`avahi-browse --all --terminate --parsable`

- List domains in the neighbourhood:

`avahi-browse --browse-domains`

- Limit the search to a particular domain:

`avahi-browse --all --domain={{domain}}`
