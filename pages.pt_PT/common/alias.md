# alias

> Cria um alias -- palavras que são substituídas por um comando.
> Alias expiram com a sessão da shell atual, a menos que sejam definidos no ficheiro de configuração da shell, por exemplo `~/.bashrc`.
> Mais informações: <https://tldp.org/LDP/abs/html/aliases.html>.

- Lista todos os alias:

`alias`

- Cria um alias genérico:

`alias {{palavra}}="{{comando}}"`

- Visualiza o comando associado a um dado alias:

`alias {{palavra}}`

- Remove um alias de um comando:

`unalias {{palavra}}`

- Torna `rm` num comando interativo:

`alias {{rm}}="{{rm -i}}"`

- Cria `la` como um atalho para `ls -a`:

`alias {{la}}="{{ls -a}}"`
