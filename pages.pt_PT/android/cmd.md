# cmd

> Gestor de serviços (service manager) do Android.
> Mais informações: <https://cs.android.com/android/platform/superproject/+/main:frameworks/native/cmds/cmd/>.

- Lista todos os serviços em execução:

`cmd -l`

- Executa um serviço específico:

`cmd {{alarm}}`

- Executa um serviço com parâmetros:

`cmd {{vibrator}} {{vibrate 300}}`
