# cmd

> O interpretador de comandos do Windows.
> Mais informações: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmd>.

- Inicia nova instância do interpretador de comandos:

`cmd`

- Executa o comando especificado e sai do interpretador:

`cmd /c "{{comando}}"`

- Executa o comando especificado e entra no shell interativo:

`cmd /k "{{comando}}"`

- Desabilita o uso do comando `echo` na saída dos comandos:

`cmd /q`

- Habilita ou desabilita extensão de comandos:

`cmd /e:{{on|off}}`

- Habilita ou desabilita a ferramenta que completa automaticamente o nome de arquivos ou diretórios:

`cmd /f:{{on|off}}`

- Habilita ou desabilita a expansão de variáveis de ambiente:

`cmd /v:{{on|off}}`

- Forçar que a saída de comandos use o padrão Unicode:

`cmd /u`
