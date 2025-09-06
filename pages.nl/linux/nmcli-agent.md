# nmcli agent

> Draai `nmcli` als een NetworkManager secret/polkit agent.
> Meer informatie: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html#agent>.

- Registeer `nmcli` als een secret agent en luister naar geheime verzoeken:

`nmcli {{[a|agent]}} {{[s|secret]}}`

- Registreer `nmcli` als een polkit agent en luister naar authorizatie verzoeken:

`nmcli {{[a|agent]}} {{[p|polkit]}}`

- Registreer `nmcli` als een secret agent en als een polkit agent:

`nmcli {{[a|agent]}} {{[a|all]}}`
