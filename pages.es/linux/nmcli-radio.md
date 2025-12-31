# nmcli radio

> Muestra el estado de los interruptores de radio o activa/desactiva utilizando NetworkManager.
> Más información: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html#radio>.

- Muestra el estado de WiFi:

`nmcli {{[r|radio]}} {{[w|wifi]}}`

- Enciende o apaga WiFi:

`nmcli {{[r|radio]}} {{[w|wifi]}} {{on|off}}`

- Muestra el estado de WWAN:

`nmcli {{[r|radio]}} {{[ww|wwan]}}`

- Enciende o apaga WWAN:

`nmcli {{[r|radio]}} {{[ww|wwan]}} {{on|off}}`

- Muestra el estado de todos los interruptores:

`nmcli {{[r|radio]}}`

- Activa o apaga todos los interruptores:

`nmcli {{[r|radio]}} {{[a|all]}} {{on|off}}`
