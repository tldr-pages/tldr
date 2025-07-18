# nmcli device

> Manage network interfaces and establish new Wi-Fi connections using NetworkManager.
> More information: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>.

- Print the statuses of all network interfaces:

`nmcli {{[d|device]}}`

- Print the available Wi-Fi access points:

`nmcli {{[d|device]}} wifi`

- Connect to a Wi-Fi network with the specified SSID (you will be prompted for a password):

`nmcli {{[d|device]}} wifi connect {{ssid}} --ask`

- Print the password and QR code for the current Wi-Fi network:

`nmcli {{[d|device]}} wifi show-password`
