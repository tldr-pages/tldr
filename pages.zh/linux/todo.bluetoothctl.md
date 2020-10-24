# bluetoothctl

> Handling bluetooth devices from the shell.

- Enter the bluetoothctl shell:

`bluetoothctl`

- List devices:

`bluetoothctl -- devices`

- Pair a device:

`bluetoothctl -- pair {{mac_address}}`

- Remove a device:

`bluetoothctl -- remove {{mac_address}}`

- Connect a paired device:

`bluetoothctl -- connect {{mac_address}}`

- Disconnect a paired device:

`bluetoothctl -- disconnect {{mac_address}}`
