# scutil

> Gere parametros da configuração do sistema.
> Necessita de permissões de root para modificar configurações.

- Mostra as configurações de DNS:

`scutil --dns`

- Mostra as configurações de proxy:

`scutil --proxy`

- Obtêm o nome do computador:

`scutil --get ComputerName`

- Altera o nome do computador:

`sudo scutil --set ComputerName {{computer_name}}`

- Obtêm o nome de rede do computador:

`scutil --get HostName`

- Altera o nome de rede do computador:

`scutil --set HostName {{hostname}}`
