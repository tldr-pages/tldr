# nmcli general

> Beheer algemene instellingen van NetworkManager.
> Dit subcommando kan ook aangeroepen worden met `nmcli g`.
> Meer informatie: <https://networkmanager.dev/docs/api/latest/nmcli.html>.

- Toon de algemene status van NetworkManager:

`nmcli general`

- Toon de hostname van het huidige apparaat:

`nmcli general hostname`

- Verander de hostname van het huidige apparaat:

`sudo nmcli general hostname {{new_hostname}}`

- Toon de permissies van NetworkManager:

`nmcli general permissions`

- Toon het huidige logging level en domeinen:

`nmcli general logging`

- Zet het logging level en/of domainen (zie `man NetworkManager.conf` voor alle beschikbare domeinen):

`nmcli general logging level {{INFO|OFF|ERR|WARN|DEBUG|TRACE}} domain {{domein_1,domein_2,...}}`
