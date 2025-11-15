# cmd

> O interpretador de comandos do Windows.
> Mais informações: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmd>.

- Inicia uma sessão do interpretador de comandos:

`cmd`

- Executa os [c]omandos especificados:

`cmd /c {{echo Olá Mundo}}`

- Executa um script específico:

`cmd {{caminho/para/script.bat}}`

- Executa o comando especificado e entra em um shell interativo:

`cmd /k {{echo Olá Mundo}}`

- Entra em um shell interativo e desabilita o uso do comando `echo` na saída dos comandos:

`cmd /q`

- Entra em um shell interativo com ou a expansão de [v]ariáveis de ambiente habilitada ou desabilitada:

`cmd /v:{{on|off}}`

- Entra em um shell interativo com a extensão de comandos habilitada ou desabilitada:

`cmd /e:{{on|off}}`

- Entra em um shell interativo com a saída de comandos no padrão Unicode:

`cmd /u`
