# nmcli device

> Gestionarea dispozitivelor hardware cu NetworkManager.
> Mai multe informaţii: <https://man.archlinux.org/man/nmcli.1>

- Imprimați stările tuturor interfețelor de rețea:

`nmcli device status`

- Imprimați punctele de acces Wi-Fi disponibile:

`nmcli device wifi`

- Conectați-vă la rețeaua Wi-Fi cu un nume și o parolă specificate:

`nmcli device wifi connect {{ssid}} password {{password}}`

- Imprimați parola și codul QR pentru rețeaua Wi-Fi curentă:

`nmcli device wifi show-password`
