# logcat

> Exibe um conjunto de mensagens de sistema, incluindo a stack de execução do programa em caso de erro, e mensagens de informação criadas por aplicações.
> Mais informações: <https://developer.android.com/studio/command-line/logcat>.

- Mostrar mensagens de sistema:

`logcat`

- Escrever as mensagens de sistema num ficheiro:

`logcat -f {{caminho/para/arquivo}}`

- Mostrar mensagens que correspondem a uma expressão regular:

`logcat --regex {{expressao_regular}}`
