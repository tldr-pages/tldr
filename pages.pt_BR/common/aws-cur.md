# aws cur

> Cria, pesquisa e apaga relatórios de uso do AWS.
> Mais informações: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/index.html>.

- Cria um relatório de uso e custo do AWS definido de a partir de um arquivo JSON:

`aws cur put-report-definition --report-definition file://{{caminho/para/definição_do_relatório.json}}`

- Lista as definições dos relatórios de uso para a conta logada:

`aws cur describe-report-definitions`

- Apaga uma definição de relatório de uso:

`aws cur --region {{região_aws}} delete-report-definition --report-name {{relatório}}`
