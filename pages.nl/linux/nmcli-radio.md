# nmcli radio

> Toon de status van radioschakelaars of schakel ze in/uit via NetworkManager.
> Dit subcommando kan ook aangeroepen worden met `nmcli r`.
> Meer informatie: <https://networkmanager.dev/docs/api/latest/nmcli.html>.

- Toon de status van Wi-Fi:

`nmcli radio wifi`

- Zet Wi-Fi aan of uit:

`nmcli radio wifi {{on|off}}`

- Toon de status van WWAN:

`nmcli radio wwan`

- Zet WWAN aan of uit:

`nmcli radio wwan {{on|off}}`

- Toon de status van beide switches:

`nmcli radio all`

- Zet beide switches aan of uit:

`nmcli radio all {{on|off}}`
