# afplay

> Player de áudio para linha de comando.
> Mais informações: <https://keith.github.io/xcode-man-pages/afplay.1.html>.

- Reproduz um arquivo de som (espera até que a reprodução termine):

`afplay {{caminho/para/arquivo}}`

- Reproduz um arquivo de som em velocidade 2x (taxa de reprodução):

`afplay --rate {{2}} {{caminho/para/arquivo}}`

- Reproduz um arquivo de som em meia velocidade:

`afplay --rate {{0.5}} {{caminho/para/arquivo}}`

- Reproduz os N primeiros segundos de um arquivo de som:

`afplay --time {{segundos}} {{caminho/para/arquivo}}`
