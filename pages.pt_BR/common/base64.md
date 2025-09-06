# base64

> Codifica ou decodifica um arquivo ou a entrada padrão (`stdin`) de/para Base64, para a saída padrão (`stdout`).
> Mais informações: <https://manned.org/base64>.

- Codifica um arquivo:

`base64 {{caminho/para/arquivo}}`

- Envolve a saída codificada em uma largura específica (`0` desabilita o encapsulamento):

`base64 {{[-w|--wrap]}} {{0|76|...}} {{caminho/para/arquivo}}`

- Decodifica um arquivo:

`base64 {{[-d|--decode]}} {{caminho/para/arquivo}}`

- Codifica a partir de `stdin`:

`{{algum_comando}} | base64`

- Decodifica a partir de `stdin`:

`{{algum_comando}} | base64 {{[-d|--decode]}}`
