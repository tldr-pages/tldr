# hexdump

> Impressão de dados no formato ASCII, decimal, hexadecimal ou octal.
> Mais informações: <https://manned.org/hexdump>.

- Imprime a representação hexadecimal de um arquivo, substituindo linhas duplicadas por '*':

`hexdump {{nome_do_arquivo}}`

- Imprime a representação hexadecimal e ASCII de um arquivo, em duas colunas:

`hexdump -C {{nome_do_arquivo}}`

- Imprime a representação hexadecimal de um arquivo, porém apresentando apenas seus n primeiros bytes:

`hexdump -C -n{{numero_de_bytes}} {{nome_do_arquivo}}`

- Não substitui as linhas duplicadas por '*':

`hexdump --no-squeezing {{nome_do_arquivo}}`
