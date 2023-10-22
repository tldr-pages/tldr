# cmd

> Gestor de serviços (service manager) do Android.
> Mais informações: <https://cs.android.com/android/platform/superproject/+/main:frameworks/native/cmds/cmd/>.

- Listar todos os serviços em execução:

`cmd -l`

- Executar um serviço específico:

`cmd {{alarm}}`

- Executar um serviço com parâmetros:

`cmd {{vibrator}} {{vibrate 300}}`
