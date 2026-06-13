# nmcli general

> Spravuje obecné nastavení NetworkManageru.
> Tento dílčí příkaz může být zvolán také pomocí `nmcli g`.
> Více informací: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html#general>.

- Zobrazit obecný stav NetworkManageru:

`nmcli {{[g|general]}}`

- Zobrazit hostitelské jméno aktuálního zařízení:

`nmcli {{[g|general]}} {{[h|hostname]}}`

- Změnit hostitelské jméno aktuálního zařízení:

`sudo nmcli {{[g|general]}} {{[h|hostname]}} {{nove_hostitelske_jmeno}}`

- Zobrazit oprávění NetworkManageru:

`nmcli {{[g|general]}} {{[p|permissions]}}`

- Zobrazit aktuální úroveň logů a domén:

`nmcli {{[g|general]}} {{[l|logging]}}`

- Nastavit úroveň logů a/nebo domén (všechny dostupné domény najdete pomocí `man NetworkManager.conf`):

`sudo nmcli {{[g|general]}} {{[l|logging]}} {{[l|level]}} {{INFO|OFF|ERR|WARN|DEBUG|TRACE}} domain {{domena_1,domena_2,...}}`
