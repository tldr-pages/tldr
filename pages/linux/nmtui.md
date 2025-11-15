# nmtui

> Text user interface for controlling NetworkManager.
> Use `<ArrowKeys>` to navigate, `<Enter>` to select an option.
> See also: `nmcli`.
> More information: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmtui.html>.

- Open the user interface:

`nmtui`

- List available connections, with the option to activate or deactivate them:

`nmtui connect`

- Connect to a given network:

`nmtui connect {{name|uuid|device|SSID}}`

- Edit/Add/Delete a given network:

`nmtui edit {{name|id}}`

- Set the system hostname:

`nmtui hostname`
