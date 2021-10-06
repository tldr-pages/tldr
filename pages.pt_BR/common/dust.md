# dust

> Dust oferece uma visão geral de quais diretórios estão usando espaço em disco.
> Mais informações: <https://github.com/bootandy/dust>.

- Exibir informações para o diretório atual:

`dust`

- Exibir informações para uma lista de diretórios separados por espaço:

`dust {{caminho/para/diretório1}} {{caminho/para/diretório2}}`

- Exibir 30 diretórios (o padrão é 21):

`dust --number-of-lines {{30}}`

- Exibir informações para o diretório atual, com até 3 níveis de profundidade:

`dust --depth {{3}}`

- Exibir os maiores diretórios no topo em ordem decrescente:

`dust --reverse`

- Ignorar todos os arquivos e diretórios com um nome específico:

`dust --ignore-directory {{arquivo_ou_nome_do_diretório}}`

- Não exibir barras de porcentagem e porcentagens:

`dust --no-percent-bars`
