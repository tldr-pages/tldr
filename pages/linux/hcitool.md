# hcitool

> Monitor & Configure Bluetooth connections.
> Send special commands to Bluetooth devices.

- Scan for Bluetooth devices:

`hcitool scan`

- Output the name of a device specifying its MAC address:

`hcitool name {{bdaddr}}`

- Fetch information about a remote Bluetooth device:

`hcitool info {{bdaddr}}`

- Check the link quality to a Bluetooth device:

`hcitool lq {{bdaddr}}`

- Display the transmit power level:

`hcitool tpl {{bdaddr}} {{type}}`

- Display the link policy:

`hcitool lp`

- Request authentication with a specific device:

`hcitool auth {{bdaddr}}`

- Display local devices:

`hcitool dev`
