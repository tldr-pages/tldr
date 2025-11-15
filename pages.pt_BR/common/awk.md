# awk

> Uma linguagem de programação versátil para trabalhar com arquivos.
> Mais informações: <https://github.com/onetrueawk/awk>.

- Imprime a quinta coluna (também chamada de campo) em um arquivo separado por espaços:

`awk '{print $5}' {{caminho/para/arquivo}}`

- Imprime a segunda coluna das linhas contendo "foo" em um arquivo separado por espaços:

`awk '/{{foo}}/ {print $2}' {{caminho/para/arquivo}}`

- Imprime a última coluna de cada linha em um arquivo, usando vírgula (ao invés de espaço) como separador de campo:

`awk -F ',' '{print $NF}' {{caminho/para/arquivo}}`

- Soma os valores da primeira coluna de um arquivo e imprime o total:

`awk '{s+=$1} END {print s}' {{caminho/para/arquivo}}`

- Imprime de três em três linhas a partir da primeira:

`awk 'NR%3==1' {{caminho/para/arquivo}}`

- Imprime diferentes valores baseado em condições:

`awk '{if ($1 == "foo") print "Correspondência completa foo"; else if ($1 ~ "bar") print "Correspondência parcial bar"; else print "Baz"}' {{caminho/para/arquivo}}`

- Imprime todas as linhas em que o valor da décima coluna está entre um mínimo e um máximo:

`awk '($10 >= {{valor_minimo}} && $10 <= {{valor_maximo}})'`

- Imprime tabela de usuários com UID >=1000 com cabeçalho e saída formatada, usando dois pontos como separador (`%-20s` significa: alinhamento à esquerda de 20 caracteres, `%6s` significa: alinhamento à direita 6 caracteres):

`awk 'BEGIN {FS=":";printf "%-20s %6s %25s\n", "Nome", "UID", "Shell"} $4 >= 1000 {printf "%-20s %6d %25s\n", $1, $4, $7}' /etc/passwd`
