# act

> Executa GitHub Actions localmente utilizando Docker.
> Mais informações: <https://github.com/nektos/act>.

- Lista ações disponíveis:

`act -l`

- Executa evento padrão:

`act`

- Executa evento específico:

`act {{tipo_de_evento}}`

- Executa ação específica:

`act -a {{acao_id}}`

- Executa job específico:

`act -j {{job_id}}`

- Não executa realmente as açoes (i.e. um dry run):

`act -n`

- Mostra verbose logs:

`act -v`

- Executa um Workflow específico com o evento de push.

`act push -W {{path/to/workflow}}`
