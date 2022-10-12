# dumpsys

> Fornece informações sobre os serviços do sistema Android.
> Este comando só pode ser usado com a `adb shell`.
> Mais informações: <https://developer.android.com/studio/command-line/dumpsys>.

- Gerar um diagnóstico de todos os serviços do sistema:

`dumpsys`

- Gerar um diagnóstico de um serviço do sistema específico:

`dumpsys {{servico}}`

- Listar todos os serviços dos quais o `dumpsys` pode obter informações:

`dumpsys -l`

- Listar argumentos específicos de um serviço para um serviço:

`dumpsys {{servico}} -h`

- Omitir um serviço em específico do diagnóstico:

`dumpsys --skip {{servico}}`

- Especificar um periodo de _timeout_ (por padrão é 10s):

`dumpsys -t {{segundos}}`
