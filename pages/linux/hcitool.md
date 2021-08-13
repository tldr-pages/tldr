# hcitool

> Monitor & Configure Bluetooth connections.
> Send special commands to Bluetooth devices.

- Scan for remote devices:

`hcitool scan`

- Output name of the device with its mac address:

`hcitool name {{bdaddr}}`

- Fetch info of a remote bluetooth device:

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
