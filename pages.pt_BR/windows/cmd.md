# cmd

> O interpretador de comandos do Windows.
> Mais informações: <https://docs.microsoft.com/windows-server/administration/windows-commands/cmd>.

- Iniciar nova instância do interpretador de comandos:

`cmd`

- Executar o comando especificado e sair do interpretador:

`cmd /c "{{comando}}"`

- Executar o comando especificado e entrar no shell interativo:

`cmd /k "{{comando}}"`

- Desabilitar o uso do comando `echo` na saída dos comandos:

`cmd /q`

- Habilitar ou desabilitar extensão de comandos:

`cmd /e:{{on|off}}`

- Habilitar ou desabilitar a ferramenta que completa automaticamente o nome de arquivos ou diretórios:

`cmd /f:{{on|off}}`

- Habilitar ou desabilitar a expansão de variáveis de ambiente:

`cmd /v:{{on|off}}`

- Forçar que a saída de comandos use o padrão Unicode:

`cmd /u`
