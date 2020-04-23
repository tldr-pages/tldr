# alias

> Cria apelidos -- palavras que são substituídas por um comando.
> Apelidos expiram ao final da sessão atual do shell de comando, a menos que sejam definidos no arquivo de configuração do shell, por exemplo `~/.bashrc`.

- Criar um apelido:

`alias {{apelido}}="{{comando}}"`

- Visualizar o comando associado a um determinado apelido:

`alias {{apelido}}`

- Remover um apelido:

`unalias {{apelido}}`

- Exibir todos os apelidos definidos:

`alias -p`

- Tornar o comando `rm` interativo:

`alias {{rm}}="{{rm -i}}"`

- Criar o apelido `la` como um atalho para `ls -a`:

`alias {{la}}="{{ls -a}}"`
