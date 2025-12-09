# hcitool

> Monitor, configure connections, and send special commands to Bluetooth devices.
> More information: <https://manned.org/hcitool>.

- Scan for Bluetooth devices:

`hcitool scan`

- Output the name of a device, returning its MAC address:

`hcitool name {{bdaddr}}`

- Fetch information about a remote Bluetooth device:

`hcitool info {{bdaddr}}`

- Check the link quality to a Bluetooth device:

`hcitool lq {{bdaddr}}`

- Modify the transmit power level:

`hcitool tpl {{bdaddr}} {{0|1}}`

- Display the link policy:

`hcitool lp`

- Request authentication with a specific device:

`hcitool auth {{bdaddr}}`

- Display local devices:

`hcitool dev`
