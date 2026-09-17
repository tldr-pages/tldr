# apropos

> Busca nomes e descrições nas páginas de manual.
> Veja também: `man`.
> Mais informações: <https://manned.org/apropos>.

- Busca por uma palavra-chave usando uma `regex`:

`apropos {{regex}}`

- Busca sem limitar a saída à largura do terminal (saída longa):

`apropos {{[-l|--long]}} {{regex}}`

- Busca páginas que correspondem a todas as `regex` fornecidas:

`apropos {{regex_1}} {{[-a|--and]}} {{regex_2}} {{[-a|--and]}} {{regex_3}}`
