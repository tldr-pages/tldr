# dumpsys

> Fornece informações sobre os serviços do sistema Android.
> Este comando só pode ser usado através de `adb shell`.
> Mais informações: <https://developer.android.com/studio/command-line/dumpsys>.

- Gera um diagnóstico de todos os serviços do sistema:

`dumpsys`

- Gera um diagnóstico de um serviço do sistema específico:

`dumpsys {{serviço}}`

- Lista todos os serviços que o `dumpsys` pode obter informações:

`dumpsys -l`

- Lista argumentos específicos-de-um-serviço para um serviço:

`dumpsys {{serviço}} -h`

- Omite um serviço em específico do diagnóstico:

`dumpsys --skip {{serviço}}`

- Específica um periodo de _timeout_ (por padrão é 10s):

`dumpsys -t {{segundos}}`
