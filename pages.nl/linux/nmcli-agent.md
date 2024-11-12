# nmcli agent

> Draai `nmcli` als een NetworkManager secret/polkit agent.
> Dit subcommando kan ook aangeroepen worden met `nmcli a`.
> Meer informatie: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>.

- Registeer `nmcli` als een secret agent en luister naar geheime verzoeken:

`nmcli agent secret`

- Registreer `nmcli` als een polkit agent en luister naar authorizatie verzoeken:

`nmcli agent polkit`

- Registreer `nmcli` als een secret agent en als een polkit agent:

`nmcli agent all`
