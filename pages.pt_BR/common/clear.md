# clear

> Limpa a tela do terminal.
> Mais informações: <https://manned.org/clear>.

- Limpa a tela (equivalente a apertar Control-L no terminal Bash):

`clear`

- Limpa a tela mantendo o buffer de rolagem do terminal:

`clear -x`

- Especifica o tipo de terminal a ser limpado (por padrão é o valor da variável de ambiente `TERM`):

`clear -T {{tipo_do_terminal}}`

- Mostra a versão do `ncurses` usado pelo `clear`:

`clear -V`
