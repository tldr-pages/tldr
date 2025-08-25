# bluetoothctl

> Spravuje Bluetooth zařízení.
> Více informací: <https://manned.org/bluetoothctl>.

- Vstoupit do `bluetoothctl` shellu:

`bluetoothctl`

- Vypsat všechny známe zařízení:

`bluetoothctl devices`

- Zapnout nebo vypnout Bluetooth ovladač:

`bluetoothctl power {{on|off}}`

- Spárovat se s zařízením:

`bluetoothctl pair {{mac_adresa}}`

- Smazat zařízení:

`bluetoothctl remove {{mac_adresa}}`

- Připojit se ke spárovanému zařízení:

`bluetoothctl connect {{mac_adresa}}`

- Odpojit se od spárovaného zařízení:

`bluetoothctl disconnect {{mac_adresa}}`

- Zobrazit nápovědu:

`bluetoothctl help`
