# sdptool

> Query Bluetooth devices for the services they offer via SDP (Service Discovery Protocol).
> The target device must be connected or reachable.
> Part of BlueZ. See also: `bluetoothctl devices`.
> More information: <https://manned.org/sdptool>.

- List all services on a remote Bluetooth device:

`sdptool browse {{00:11:22:33:44:55}}`

- List all services on a remote device, displayed as a tree:

`sdptool browse --tree {{00:11:22:33:44:55}}`

- Search for devices offering a predefined service such as `SP`, `DUN`, `HID`, `A2SNK`, or `FTP`:

`sdptool search {{service_abbreviation}}`

- Retrieve all service records from a remote device as XML:

`sdptool records --xml {{00:11:22:33:44:55}}`
