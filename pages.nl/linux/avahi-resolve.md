# avahi-resolve

> Vertaal tussen hostnamen en IP-adressen.
> Meer informatie: <https://manned.org/avahi-resolve>.

- Zet een lokale service om naar zijn IPv4-adres:

`avahi-resolve -4 {{[-n|--name]}} {{service.local}}`

- Vertaal een IP naar een hostnaam, verbose:

`avahi-resolve {{[-v|--verbose]}} {{[-a|--address]}} {{IP}}`
