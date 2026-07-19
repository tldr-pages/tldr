# hexdump

> Imprime dados no formato ASCII, decimal, hexadecimal ou octal.
> Veja também: `hexyl`, `od`, `xxd`.
> Mais informações: <https://manned.org/hexdump>.

- Imprime a representação hexadecimal de um arquivo, substituindo linhas duplicadas por '*':

`hexdump {{caminho/para/arquivo}}`

- Imprime a representação hexadecimal e ASCII de um arquivo, em duas colunas:

`hexdump {{[-C|--canonical]}} {{caminho/para/arquivo}}`

- Imprime a representação hexadecimal de um arquivo, porém apresentando apenas seus n primeiros bytes:

`hexdump {{[-C|--canonical]}} {{[-n|--length]}} {{numero_de_bytes}} {{caminho/para/arquivo}}`

- Imprime a representação hexadecimal completa de um arquivo (sem omitir linhas duplicadas):

`hexdump {{[-v|--no-squeezing]}} {{caminho/para/arquivo}}`
