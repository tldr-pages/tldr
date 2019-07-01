# nmcli

> A command line tool for controlling NetworkManager.

- List all NetworkManager connections (shows name, uuid, type and device):

`nmcli connection`

- Print the available Wi-Fi access points:

`nmcli device wifi`

- Connect to the Wi-Fi network with a specified name and password:

`nmcli device wifi connect {{name}} {{password}}`

- Activate a connection by specifying an uuid:

`nmcli connection up uuid {{uuid}}`

- Deactivate a connection:

`nmcli connection down uuid {{uuid}}`

- Print statuses of network interfaces:

`nmcli device status`
