# nmcli networking

> Spravuje síťový stav NetworkManageru.
> Více informací: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html#networking>.

- Zobrazit síťový stav NetworkManageru:

`nmcli {{[n|networking]}}`

- Povolit nebo zakázat síťování a všechny rozhraní spravované NetworkManagerem:

`nmcli {{[n|networking]}} {{on|off}}`

- Zobrazit poslední známý stav připojení:

`nmcli {{[n|networking]}} {{[c|connectivity]}}`

- Zobrazit aktuální stav připojení:

`nmcli {{[n|networking]}} {{[c|connectivity]}} {{[c|check]}}`
