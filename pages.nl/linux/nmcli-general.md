# nmcli general

> Beheer algemene instellingen van NetworkManager.
> Meer informatie: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html#general>.

- Toon de algemene status van NetworkManager:

`nmcli {{[g|general]}}`

- Toon de hostname van het huidige apparaat:

`nmcli {{[g|general]}} {{[h|hostname]}}`

- Verander de hostname van het huidige apparaat:

`sudo nmcli {{[g|general]}} {{[h|hostname]}} {{nieuwe_hostnaam}}`

- Toon de permissies van NetworkManager:

`nmcli {{[g|general]}} {{[p|permissions]}}`

- Toon het huidige logging level en domeinen:

`nmcli {{[g|general]}} {{[l|logging]}}`

- Zet het logging level en/of domainen (zie `man NetworkManager.conf` voor alle beschikbare domeinen):

`sudo nmcli {{[g|general]}} {{[l|logging]}} {{[l|level]}} {{INFO|OFF|ERR|WARN|DEBUG|TRACE}} domain {{domein_1,domein_2,...}}`
