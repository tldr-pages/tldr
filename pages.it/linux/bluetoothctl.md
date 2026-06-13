# bluetoothctl

> Gestisce i dispositivi Bluetooth.
> Vedi anche: `bluetui`.
> Maggiori informazioni: <https://manned.org/bluetoothctl>.

- Entra nella shell `bluetoothctl`:

`bluetoothctl`

- Elenca tutti i dispositivi conosciuti:

`bluetoothctl devices`

- Accende o spegne il controller Bluetooth:

`bluetoothctl power {{on|off}}`

- Effettua il pairing con un dispositivo:

`bluetoothctl pair {{mac_address}}`

- Rimuove un dispositivo:

`bluetoothctl remove {{mac_address}}`

- Connetti a un dispositivo associato:

`bluetoothctl connect {{mac_address}}`

- Disconnetti da un dispositivo associato:

`bluetoothctl disconnect {{mac_address}}`

- Mostra l'aiuto:

`bluetoothctl help`
