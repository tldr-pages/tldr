# base64

> Codifica ou decodifica arquivo ou `stdin` de/para base64, para `stdout` ou outro arquivo.
> Mais informações: <https://man.freebsd.org/cgi/man.cgi?query=base64>.

- Codifica um arquivo para `stdout`:

`base64 {{[-i|--input]}} {{caminho/para/arquivo}}`

- Codifica um arquivo para o arquivo de saída especificado:

`base64 {{[-i|--input]}} {{caminho/para/arquivo_de_entrada}} {{[-o|--output]}} {{caminho/para/arquivo_de_saída}}`

- Quebra (insere uma quebra de linha) a saída codificada em uma largura específica (‘0’ desabilita encapsulamento):

`base64 {{[-b|--break]}} {{0|76|...}} {{caminho/para/arquivo}}`

- Decodifica um arquivo para `stdout`:

`base64 {{[-d|--decode]}} {{[-i|--input]}} {{caminho/para/arquivo}}`

- Codifica de `stdin` para `stdout`:

`{{comando}} | base64`

- Decodifica de `stdin` para `stdout`:

`{{comando}} | base64 {{[-d|--decode]}}`
