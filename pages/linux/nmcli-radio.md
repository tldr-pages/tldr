# nmcli radio

> Show the status of radio switches or enable/disable them using NetworkManager.
> More information: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>.

- Show status of Wi-Fi:

`nmcli {{[r|radio]}} wifi`

- Turn Wi-Fi on or off:

`nmcli {{[r|radio]}} wifi {{on|off}}`

- Show status of WWAN:

`nmcli {{[r|radio]}} wwan`

- Turn WWAN on or off:

`nmcli {{[r|radio]}} wwan {{on|off}}`

- Show status of both switches:

`nmcli {{[r|radio]}} all`

- Turn both switches on or off:

`nmcli {{[r|radio]}} all {{on|off}}`
