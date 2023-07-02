# bash

> Bourne-Again SHell, um interpretador de linha de comando compatível com `sh`.
> Veja também `histexpand` para a expansão do histórico.
> Mais informações: <https://gnu.org/software/bash/>.

- Iniciar uma seção interativa do shell:

`bash`

- Executar um comando e sair:

`bash -c "{{comando}}"`

- Executar um script:

`bash {{caminho/para/script.sh}}`

- Executar um script, exibindo cada comando antes de executá-lo:

`bash -x {{caminho/para/script.sh}}`

- Executar os comandos de um script, parando de executar no primeiro erro:

`bash -e {{caminho/para/script.sh}}`

- Ler e executar comandos do `stdin` (entrada padrão):

`bash -s`

- Exibir a versão do Bash (`$BASH_VERSION` abrange apenas a versão sem informações da licença):

`bash --version`
