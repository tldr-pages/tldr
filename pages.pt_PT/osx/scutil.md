# scutil

> Gere parametros da configuração do sistema.
> Necessita de permissões de root para modificar configurações.
> Mais informações: <https://ss64.com/osx/scutil.html>.

- Mostra as configurações de DNS:

`scutil --dns`

- Mostra as configurações de proxy:

`scutil --proxy`

- Obtêm o nome do computador:

`scutil --get ComputerName`

- Altera o nome do computador:

`sudo scutil --set ComputerName {{nome_computador}}`

- Obtêm o nome de rede do computador:

`scutil --get HostName`

- Altera o nome de rede do computador:

`scutil --set HostName {{nome_rede_computador}}`
