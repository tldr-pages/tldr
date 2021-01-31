# alias

> Cria um alias -- palavras que são substituídas por um comando.
> Alias expiram com a sessão da shell atual, a menos que sejam definidos no ficheiro de configuração da shell, por exemplo `~/.bashrc`.

- Listar todos os alias:

`alias`

- Criar um alias genérico:

`alias {{palavra}}="{{comando}}"`

- Visualizar o comando associado a um dado alias:

`alias {{palavra}}`

- Remover um alias de um comando:

`unalias {{palavra}}`

- Tornar `rm` num comando interativo:

`alias {{rm}}="{{rm -i}}"`

- Criar `la` como um atalho para `ls -a`:

`alias {{la}}="{{ls -a}}"`
