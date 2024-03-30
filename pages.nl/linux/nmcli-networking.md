# nmcli networking

> Beheer de netwerk status of NetworkManager.
> Dit subcommando kan ook aangeroepen worden met `nmcli n`.
> Meer informatie: <https://networkmanager.dev/docs/api/latest/nmcli.html>.

- Toon de netwerk status of NetworkManager:

`nmcli networking`

- Schakel netwerk in/uit en alle interfaces die worden beheerd door NetworkManager:

`nmcli networking {{on|off}}`

- Toon de laatst bekende connectiviteit status:

`nmcli networking connectivity`

- Toon de huidige connectiviteit status:

`nmcli networking connectivity check`
