# dust

> Dust oferece uma visão geral de quais diretórios estão usando espaço em disco.
> Mais informações: <https://github.com/bootandy/dust>.

- Exibe informações para o diretório atual:

`dust`

- Exibe informações para uma lista de diretórios separados por espaço:

`dust {{caminho/para/diretório1}} {{caminho/para/diretório2}}`

- Exibe 30 diretórios (o padrão é 21):

`dust --number-of-lines {{30}}`

- Exibe informações para o diretório atual, com até 3 níveis de profundidade:

`dust --depth {{3}}`

- Exibe os maiores diretórios no topo em ordem decrescente:

`dust --reverse`

- Ignora todos os arquivos e diretórios com um nome específico:

`dust --ignore-directory {{arquivo_ou_nome_do_diretório}}`

- Não exibe barras de porcentagem e porcentagens:

`dust --no-percent-bars`
