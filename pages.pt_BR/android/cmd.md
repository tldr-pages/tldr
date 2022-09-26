# cmd

> Gerenciador de serviços do Android (service manager).
> Mais informações: <https://cs.android.com/android/platform/superproject/+/master:frameworks/native/cmds/cmd/>.

- Lista todos os serviços em execução:

`cmd -l`

- Chama um serviço específico:

`cmd {{alarm}}`

- Chama um serviço com parâmetros:

`cmd {{vibrator}} {{vibrate 300}}`
