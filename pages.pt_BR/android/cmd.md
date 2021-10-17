# cmd

> Gerenciador de serviços do Android (service manager).
> Mais informações: <https://cs.android.com/android/platform/superproject/+/master:frameworks/native/cmds/cmd/>.

- Listar todos os serviços em execução:

`cmd -l`

- Chamar um serviço específico:

`cmd {{alarm}}`

- Chamar um serviço com parâmetros:

`cmd {{vibrator}} {{vibrate 300}}`
