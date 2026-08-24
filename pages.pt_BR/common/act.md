# act

> Executa GitHub Actions localmente utilizando Docker.
> Mais informações: <https://manned.org/act>.

- Lista ações disponíveis:

`act {{[-l|--list]}}`

- Executa evento padrão:

`act`

- Executa evento específico:

`act {{tipo_de_evento}}`

- Executa um job específico:

`act {{[-j|--job]}} {{job_id}}`

- Não executa realmente as ações (ex.: um dry run):

`act {{[-n|--dryrun]}}`

- Mostra verbose logs:

`act {{[-v|--verbose]}}`

- Executa um workflow específico com o evento de push:

`act push {{[-W|--workflows]}} {{caminho/para/workflow}}`
