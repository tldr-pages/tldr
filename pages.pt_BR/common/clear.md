# clear

> Limpa a tela do terminal.
> Mais informações: <https://manned.org/clear>.

- Limpar a tela (equivalente a apertar Control-L no terminal Bash):

`clear`

- Limpar a tela mantendo o buffer de rolagem do terminal:

`clear -x`

- Especificar o tipo de terminal a ser limpado (por padrão é o valor da variável de ambiente `TERM`):

`clear -T {{tipo_do_terminal}}`

- Mostra a versão do `ncurses` usado pelo `clear`:

`clear -V`
