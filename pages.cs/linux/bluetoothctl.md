# bluetoothctl

> Spravuje Bluetooth zařízení.
> Více informací: <https://manned.org/bluetoothctl>.

- Vstoupit do `bluetoothctl` shellu:

`bluetoothctl`

- Vypsat všechna známá zařízení:

`bluetoothctl devices`

- Zapnout nebo vypnout Bluetooth ovladač:

`bluetoothctl power {{on|off}}`

- Spárovat se zařízením:

`bluetoothctl pair {{mac_adresa}}`

- Smazat zařízení:

`bluetoothctl remove {{mac_adresa}}`

- Připojit se k spárovanému zařízení:

`bluetoothctl connect {{mac_adresa}}`

- Odpojit se od spárovaného zařízení:

`bluetoothctl disconnect {{mac_adresa}}`

- Zobrazit nápovědu:

`bluetoothctl help`
