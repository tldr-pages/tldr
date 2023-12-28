# csplit

> Divide um arquivo em várias partes.
> O padrão de nomenclatura dos arquivos será "xx00", "xx01" e assim por diante.
> Mais informações: <https://www.gnu.org/software/coreutils/csplit>.

- Divide um arquivo nas linhas 5 e 23:

`csplit {{arquivo}} {{5}} {{23}}`

- Divide um arquivo a cada 5 linhas (este comando irá falhar se o total de linhas do arquivo não for divisível por 5):

`csplit {{arquivo}} {{5}} {*}`

- Divide um arquivo a cada 5 linhas, ignorando o fato do total de linhas ser divisível por 5:

`csplit -k {{arquivo}} {{5}} {*}`

- Divide o arquivo na linha 5 e utiliza um prefixo específico para os arquivos de saída:

`csplit {{arquivo}} {{5}} -f {{prefix}}`

- Divide um arquivo na linha que atenda a expressão regular:

`csplit {{arquivo}} /{{expressao_regular}}/`
