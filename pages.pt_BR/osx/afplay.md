# afplay

> Player de áudio para linha de comando.
> Mais informações: <https://ss64.com/osx/afplay.html>.

- Reproduzir um arquivo de som (espera até que a reprodução termine):

`afplay {{caminho/para/arquivo}}`

- Reproduzir um arquivo de som em velocidade 2x (taxa de reprodução):

`afplay --rate {{2}} {{caminho/para/arquivo}}`

- Reproduzir um arquivo de som em meia velocidade:

`afplay --rate {{0.5}} {{caminho/para/arquivo}}`

- Reproduzir os N primeiros segundos de um arquivo de som:

`afplay --time {{segundos}} {{caminho/para/arquivo}}`
