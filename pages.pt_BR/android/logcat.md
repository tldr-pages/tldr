# logcat

> Despeja um registro de mensagens do sistema.
> Mais informações: <https://developer.android.com/studio/command-line/logcat>.

- Exibe a saída do registro:

`logcat`

- Salva a saída da mensagem de registro em um arquivo:

`logcat -f {{caminho/para/arquivo}}`

- Exibe apenas linhas em que a mensagem de registro corresponda a uma expressão regular:

`logcat --regex {{expressao_regular}}`
