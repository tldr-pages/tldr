# nmcli agent

> Ejecuta `nmcli` como agente secreto de NetworkManager o agente polkit.
> Este subcomando también se puede llamar con `nmcli a`.
> Más información: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html#agent>.

- Registra `nmcli` como agente secreto y escucha solicitudes secretas:

`nmcli {{[a|agent]}} {{[s|secret]}}`

- Registra `nmcli` como agente polkit y escucha solicitudes de autorización:

`nmcli {{[a|agent]}} {{[p|polkit]}}`

- Registra `nmcli` como agente secreto y agente de polkit:

`nmcli {{[a|agent]}} {{[a|all]}}`
