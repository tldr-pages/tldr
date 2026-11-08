# tailscale ssh

> Подключаться по SSH к машине Tailscale (только Linux).
> Больше информации: <https://tailscale.com/kb/1193/tailscale-ssh>.

- Включить/отключить SSH на хосте:

`tailscale up --ssh={{true|false}}`

- Подключиться по SSH к конкретному хосту с включённым Tailscale-SSH:

`tailscale ssh {{имя_пользователя}}@{{хост}}`
