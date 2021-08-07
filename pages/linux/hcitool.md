# hcitool

> Monitor & Configure Bluetooth connections and
> send special commands to Bluetooth devices

- Scan for remote devices:

`hcitool scan`

- Output name of the device with its mac address:

`hcitool name {{bdaddr}}`

- Fetch info of a remote bluetooth device:

`hcitool info {{bdaddr}}`

- Display active connections:

`hcitool con`

- Create connections:

`hcitool cc {{bdaddr}}`

- Check link quality:

`hcitool lq {{bdaddr}}`

- Display transmit power level:

`hcitool tpl {{bdaddr}} {{type}}`

- Check link policy:

`hcitool lp`

- Request authentication:

`hcitool auth {{bdaddr}}`

- Display local devices:

`hcitool dev`

- Submit arbitrary HCI commands:

`hcitool cmd {{parameters}}`
