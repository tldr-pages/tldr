# code

> Editor de código extensível e multi plataforma.
> Mais informações: <https://github.com/microsoft/vscode>.

- Inicia Visual Studio Code:

`code`

- Abre arquivos/diretórios específicos:

`code {{caminho/para/arquivo_ou_diretório1 caminho/para/arquivo_ou_diretório2 ...}}`

- Compara dois arquivos específicos:

`code --diff {{caminho/para/arquivo1}} {{caminho/para/arquivo2}}`

- Abre arquivos/diretórios específicos em uma nova janela:

`code --new-window {{caminho/para/arquivo_ou_diretório1 caminho/para/arquivo_ou_diretório2 ...}}`

- Instala/desinstala uma extensão específica:

`code --{{install|uninstall}}-extension {{editor.extensão}}`

- Imprime as extensões instaladas:

`code --list-extensions`

- Imprime extensões instaladas com suas versões:

`code --list-extensions --show-versions`

- Inicia o editor como um superusuário (root) enquanto armazena dados do usuário em um diretório específico:

`sudo code --user-data-dir {{caminho/para/diretório}}`
