# nmcli device

> Beheer netwerkinterfaces en zetten nieuwe Wi-Fi-verbindingen op via NetworkManager.
> Dit subcommando kan ook aangeroepen worden met `nmcli d`.
> Meer informatie: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>.

- Toon de statussen van alle netwerkinterfaces:

`nmcli device status`

- Toon alle beschikbare WiFi-toegangspunten:

`nmcli device wifi`

- Verbind met een Wi-Fi netwerk via een gespecificeerd SSID (je zal gevraagd worden voor een wachtwoord):

`nmcli --ask device wifi connect {{ssid}}`

- Toon het wachtwoord en de QR-code voor het huidige Wi-Fi netwerk:

`nmcli device wifi show-password`
