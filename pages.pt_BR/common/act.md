# act

> Executa GitHub Actions localmente utilizando Docker.
> Mais informações: <https://manned.org/act>.

- Lista ações disponíveis:

`act -l`

- Executa evento padrão:

`act`

- Executa evento específico:

`act {{tipo_de_evento}}`

- Executa um job específico:

`act -j {{job_id}}`

- Não executa realmente as ações (ex.: um dry run):

`act -n`

- Mostra verbose logs:

`act -v`

- Executa um workflow específico com o evento de push:

`act push -W {{caminho/para/workflow}}`
