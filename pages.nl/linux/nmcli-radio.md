# nmcli radio

> Toon de status van radioschakelaars of schakel ze in/uit via NetworkManager.
> Meer informatie: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html#radio>.

- Toon de status van Wi-Fi:

`nmcli {{[r|radio]}} {{[w|wifi]}}`

- Zet Wi-Fi aan of uit:

`nmcli {{[r|radio]}} {{[w|wifi]}} {{on|off}}`

- Toon de status van WWAN:

`nmcli {{[r|radio]}} {{[ww|wwan]}}`

- Zet WWAN aan of uit:

`nmcli {{[r|radio]}} {{[ww|wwan]}} {{on|off}}`

- Toon de status van beide switches:

`nmcli {{[r|radio]}}`

- Zet beide switches aan of uit:

`nmcli {{[r|radio]}} {{[a|all]}} {{on|off}}`
