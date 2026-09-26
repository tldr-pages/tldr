# nmcli device

> Spravuje síťové rozhraní a navazuje nové Wi-Fi spojení pomocí NetworkManageru.
> Více informací: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html#device>.

- Vypsat stav všech síťových rozhraní:

`nmcli {{[d|device]}}`

- Vypsat všechny dostupné přístupové body Wi-Fi:

`nmcli {{[d|device]}} {{[w|wifi]}}`

- Připojit se k Wi-Fi síťi s uvedeným SSID (budete vyzváni k zadání hesla):

`nmcli {{[d|device]}} {{[w|wifi]}} {{[c|connect]}} {{ssid}} {{[-a|--ask]}}`

- Vytvořit Wi-Fi hotspot:

`nmcli {{[d|device]}} {{[w|wifi]}} {{[ho|hotspot]}} ifname {{wlan0}} ssid "{{hotspot_ssid}}" password "{{heslo}}"`

- Vypsat heslo a QR kód pro aktuální Wi-Fi síť:

`nmcli {{[d|device]}} {{[w|wifi]}} {{[s|show-password]}}`

- Print detailed information about a device:

`nmcli {{[d|device]}} {{[sh|show]}} {{wlan0}}`
