# cmd

> O interpretador de comandos do Windows.
> Mais informações: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmd>.

- Inicia nova instância do interpretador de comandos:

`cmd`

- Executa o comando especificado e sai do interpretador:

`cmd /c {{echo Olá Mundo}}`

- Executa o comando especificado e entra no shell interativo:

`cmd /k {{echo Olá Mundo}}`

- Desabilita o uso do comando `echo` na saída dos comandos:

`cmd /q`

- Habilita ou desabilita a expansão de variáveis de ambiente:

`cmd /v:{{on|off}}`

- Habilita ou desabilita extensão de comandos:

`cmd /e:{{on|off}}`

- Forçar que a saída de comandos use o padrão Unicode:

`cmd /u`
