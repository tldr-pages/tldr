# bluetoothctl

> Spravuje Bluetooth zařízení.
> Viz také: `bluetui`.
> Více informací: <https://manned.org/bluetoothctl>.

- Vstoupit do `bluetoothctl` shellu:

`bluetoothctl`

- Vypsat všechna známá zařízení:

`bluetoothctl devices`

- Zapnout nebo vypnout Bluetooth ovladač:

`bluetoothctl power {{on|off}}`

- Vyhledat dostupné zařízeni po dobu 10 sekund:

`bluetoothctl {{[-t|--timeout]}} 10 scan on`

- Spárovat se zařízením:

`bluetoothctl pair {{mac_addresa}}`

- Připojit se k nebo odpojit se od spárovaného zařízení:

`bluetoothctl {{connect|disconnect}} {{mac_addresa}}`

- Povolit zařízení připojit se zpět:

`bluetoothctl trust {{mac_addresa}}`

- Smazat zařízení:

`bluetoothctl remove {{mac_addresa}}`
