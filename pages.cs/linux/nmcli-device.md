# nmcli device

> Spravuje síťové rozhraní a navazuje nové Wi-Fi spojení pomocí NetworkManageru.
> Tento dílčí příkaz může být zvolán také pomocí `nmcli d`.
> Více informací: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>.

- Vypsat stav všech síťových rozhraní:

`nmcli device status`

- Vypsat všechny dostupné přístupové body Wi-Fi:

`nmcli device wifi`

- Připojit se k Wi-Fi síťi s uvedeným SSID (budete vyzváni k zadání hesla):

`nmcli --ask device wifi connect {{ssid}}`

- Vypsat heslo a QR kód pro aktuální Wi-Fi síť:

`nmcli device wifi show-password`
