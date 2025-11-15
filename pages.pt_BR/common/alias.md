# alias

> Cria apelidos -- palavras que são substituídas por um comando.
> Apelidos expiram ao final da sessão atual do shell de comando, a menos que sejam definidos no arquivo de configuração do shell, por exemplo `~/.bashrc`.
> Mais informações: <https://www.gnu.org/software/bash/manual/bash.html#index-alias>.

- Lista todos os apelidos:

`alias`

- Cria um apelido genérico:

`alias {{apelido}}="{{comando}}"`

- Visualiza o comando associado a um determinado apelido:

`alias {{apelido}}`

- Remove um apelido:

`unalias {{apelido}}`

- Torna o comando `rm` interativo:

`alias {{rm}}="{{rm --interactive}}"`

- Cria o apelido `la` como um atalho para `ls --all`:

`alias {{la}}="{{ls --all}}"`
