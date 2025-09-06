# nmcli device

> Beheer netwerkinterfaces en zetten nieuwe Wi-Fi-verbindingen op via NetworkManager.
> Meer informatie: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html#device>.

- Toon de statussen van alle netwerkinterfaces:

`nmcli {{[d|device]}}`

- Toon alle beschikbare WiFi-toegangspunten:

`nmcli {{[d|device]}} {{[w|wifi]}}`

- Verbind met een Wi-Fi netwerk via een gespecificeerd SSID (je zal gevraagd worden voor een wachtwoord):

`nmcli {{[d|device]}} {{[w|wifi]}} {{[c|connect]}} {{ssid}} {{[-a|--ask]}}`

- Toon het wachtwoord en de QR-code voor het huidige Wi-Fi netwerk:

`nmcli {{[d|device]}} {{[w|wifi]}} {{[s|show-password]}}`

- Toon gedetailleerde informatie over een device:

`nmcli {{[d|device]}} {{[sh|show]}} {{wlan0}}`
