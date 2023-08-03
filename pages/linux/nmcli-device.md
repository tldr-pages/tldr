# nmcli device

> Manage network interfaces and establish new Wi-Fi connections using NetworkManager.
> This subcommand can also be called with `nmcli d`.
> More information: <https://networkmanager.dev/docs/api/latest/nmcli.html>.

- Print the statuses of all network interfaces:

`nmcli device status`

- Print the available Wi-Fi access points:

`nmcli device wifi`

- Connect to a Wi-Fi network with the specified SSID (you will be prompted for a password):

`nmcli --ask device wifi connect {{ssid}}`

- Print the password and QR code for the current Wi-Fi network:

`nmcli device wifi show-password`
