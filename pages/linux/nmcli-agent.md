# nmcli agent

> Run `nmcli` as a NetworkManager secret agent or polkit agent.
> More information: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>.

- Register `nmcli` as a secret agent and listen for secret requests:

`nmcli {{[a|agent]}} {{[s|secret]}}`

- Register `nmcli` as a polkit agent and listen for authorization requests:

`nmcli {{[a|agent]}} {{[p|polkit]}}`

- Register `nmcli` as a secret agent and a polkit agent:

`nmcli {{[a|agent]}} {{[a|all]}}`
