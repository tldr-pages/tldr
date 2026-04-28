# bluetoothctl

> Manage Bluetooth devices.
> See also: `bluetui`.
> More information: <https://manned.org/bluetoothctl>.

- Enter the `bluetoothctl` interactive shell:

`bluetoothctl`

- List all known devices:

`bluetoothctl devices`

- Power the Bluetooth controller on or off:

`bluetoothctl power {{on|off}}`

- Scan for available devices or turn the scan off:

`bluetoothctl scan {{on|off}}`

- Pair with a device:

`bluetoothctl pair {{mac_address}}`

- Connect to or disconnect from a paired device:

`bluetoothctl {{connect|disconnect}} {{mac_address}}`

- Allow the device to connect back:

`bluetoothctl trust {{mac_address}}`

- Remove a device:

`bluetoothctl remove {{mac_address}}`
