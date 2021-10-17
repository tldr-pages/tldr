# logcat

> Despeja um registro de mensagens do sistema.
> Mais informações: <https://developer.android.com/studio/command-line/logcat>.

- Ver a saída do registro:

`logcat`

- Gravar a saída da mensagem de registro em um arquivo:

`logcat -f {{path/to/file}}`

- Exibir apenas linhas em que a mensagem de registro corresponda a uma expressão regular:

`logcat --regex {{regular_expression}}`
