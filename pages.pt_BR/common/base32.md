# base32

> Codifica ou decodifica um arquivo ou a entrada padrão (`stdin`) de/para Base32, para a saída padrão (`stdout`).
> Mais informações: <https://manned.org/base32>.

- Codifica um arquivo:

`base32 {{caminho/para/arquivo}}`

- Envolve a saída codificada em uma largura específica (`0` desabilita o encapsulamento):

`base32 {{[-w|--wrap]}} {{0|76|...}} {{caminho/para/arquivo}}`

- Decodifica um arquivo:

`base32 {{[-d|--decode]}} {{caminho/para/arquivo}}`

- Codifica a partir de `stdin`:

`{{algum_comando}} | base32`

- Decodifica a partir de `stdin`:

`{{algum_comando}} | base32 {{[-d|--decode]}}`
