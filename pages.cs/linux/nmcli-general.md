# nmcli general

> Spravuje obecné nastavení NetworkManageru.
> Tento dílčí příkaz může být zvolán také pomocí `nmcli g`.
> Více informací: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>.

- Zobrazit obecný stav NetworkManageru:

`nmcli general`

- Zobrazit hostitelské jméno aktuálního zařízení:

`nmcli general hostname`

- Změnit hostitelské jméno aktuálního zařízení:

`sudo nmcli general hostname {{nove_hostitelske_jmeno}}`

- Zobrazit oprávění NetworkManageru:

`nmcli general permissions`

- Zobrazit aktuální úroveň logů a domén:

`nmcli general logging`

- Nastavit úroveň logů a/nebo domén (všechny dostupné domény najdete pomocí `man NetworkManager.conf`):

`nmcli general logging level {{INFO|OFF|ERR|WARN|DEBUG|TRACE}} domain {{domena_1,domena_2,...}}`
