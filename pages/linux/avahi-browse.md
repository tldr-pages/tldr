# avahi-browse

> Displays services and hosts exposed on the local network via mDNS/DNS-SD.
> Avahi is compatible with Bonjour (Zeroconf) found in Apple devices.
> More information: <https://www.avahi.org/>.

- List all services available on the local network along with their addresses and ports while ignoring local ones:

`avahi-browse --all --resolve --ignore-local`

- Limit your search to a particular domain:

`avahi-browse --all --domain={{domain}}`

- List all domains:

`avahi-browse --browse-domains`
