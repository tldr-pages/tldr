# nmcli agent

> Spouští `nmcli` jako skrytý nebo polkit NetworkManager agent.
> Více informací: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html#agent>.

- Registrovat `nmcli` jako skrytý agent a poslouchat tajné žádosti:

`nmcli {{[a|agent]}} {{[s|secret]}}`

- Registrovat `nmcli` jako polkit agent a poslouchat žádosti o autorizaci:

`nmcli {{[a|agent]}} {{[p|polkit]}}`

- Registrovat `nmcli` jako skrytý agent a polkit agent:

`nmcli {{[a|agent]}} {{[a|all]}}`
