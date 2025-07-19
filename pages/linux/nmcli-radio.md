# nmcli radio

> Show the status of radio switches or enable/disable them using NetworkManager.
> More information: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>.

- Show status of Wi-Fi:

`nmcli {{[r|radio]}} {{[w|wifi]}}`

- Turn Wi-Fi on or off:

`nmcli {{[r|radio]}} {{[w|wifi]}} {{on|off}}`

- Show status of WWAN:

`nmcli {{[r|radio]}} {{[ww|wwan]}}`

- Turn WWAN on or off:

`nmcli {{[r|radio]}} {{[ww|wwan]}} {{on|off}}`

- Show status of both switches:

`nmcli {{[r|radio]}}`

- Turn both switches on or off:

`nmcli {{[r|radio]}} {{[a|all]}} {{on|off}}`
