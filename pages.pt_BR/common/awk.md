# awk

> Uma linguagem de programação versátil para trabalhar com arquivos.
> Mais informações: <https://github.com/onetrueawk/awk>.

- Imprime a quinta coluna (também chamada de campo) em um arquivo separado por espaços:

`awk '{print $5}' {{nome_do_arquivo}}`

- Imprime a segunda coluna das linhas contendo "foo" em um arquivo separado por espaços:

`awk '/{{foo}}/ {print $2}' {{nome_do_arquivo}}`

- Imprime a última coluna de cada linha em um arquivo, usando vírgula (ao invés de espaço) como separador de campo:

`awk -F ',' '{print $NF}' {{nome_do_arquivo}}`

- Soma os valores da primeira coluna de um arquivo e imprime o total:

`awk '{s+=$1} END {print s}' {{nome_do_arquivo}}`

- Imprime de três em três linhas a partir da primeira:

`awk 'NR%3==1' {{nome_do_arquivo}}`

- Imprime diferentes valores baseado em condições:

`awk '{if ($1 == "foo") print "Correspondência completa foo"; else if ($1 ~ "bar") print "Correspondência parcial bar"; else print "Baz"}' {{nome_do_arquivo}}`

- Imprime todas as linhas em que a 10ª coluna é igual a um dado valor:

`awk '($10 == valor)'`

- Imprime todas as linhas em que o valor da décima coluna está entre um mínimo e um máximo:

`awk '($10 >= valor_minimo && $10 <= valor_maximo)'`
