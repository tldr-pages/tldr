# nmcli device

> Spravuje síťové rozhraní a navazuje nové Wi-Fi spojení pomocí NetworkManageru.
> Tento dílčí příkaz může být zvolán také pomocí `nmcli d`.
> Více informací: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html#device>.

- Vypsat stav všech síťových rozhraní:

`nmcli {{[d|device]}}`

- Vypsat všechny dostupné přístupové body Wi-Fi:

`nmcli {{[d|device]}} {{[w|wifi]}}`

- Připojit se k Wi-Fi síťi s uvedeným SSID (budete vyzváni k zadání hesla):

`nmcli {{[d|device]}} {{[w|wifi]}} {{[c|connect]}} {{ssid}} {{[-a|--ask]}}`

- Vypsat heslo a QR kód pro aktuální Wi-Fi síť:

`nmcli {{[d|device]}} {{[w|wifi]}} {{[s|show-password]}}`
