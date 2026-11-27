# ausearch

> Consulta eventos nos logs de auditoria do Linux.
> Parte do pacote `audit`.
> Veja também: `audit2why`, `audit2allow`, `aureport`.
> Mais informações: <https://manned.org/ausearch>.

- Pesquisa todos os eventos de negação AVC do SELinux:

`sudo ausearch {{[-m|--message]}} avc`

- Pesquisa eventos relacionados a um executável específico:

`sudo ausearch {{[-c|--comm]}} {{httpd}}`

- Pesquisa eventos de um usuário específico:

`sudo ausearch {{[-ui|--uid]}} {{1000}}`

- Pesquisa eventos nos últimos 10 minutos:

`sudo ausearch {{[-ts|--start]}} recent`

- Pesquisa tentativas de login com falha:

`sudo ausearch {{[-m|--message]}} user_login {{[-sv|--success]}} no`

- Pesquisa eventos relacionados a um arquivo específico:

`sudo ausearch {{[-f|--file]}} {{caminho/para/arquivo}}`

- Exibe os resultados em formato bruto para processamento posterior:

`sudo ausearch {{[-m|--message]}} avc --raw`
