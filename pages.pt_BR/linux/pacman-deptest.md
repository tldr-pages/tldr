# pacman --deptest

> Verifica cada dependência especificada e retorna uma lista de dependências que não estão satisfeitas atualmente no sistema.
> Veja também: `pacman`.
> Mais informações: <https://manned.org/pacman.8>.

- Imprime os nomes de pacotes das dependências que não estão instaladas:

`pacman --deptest {{pacote1 pacote2 ...}}`

- Verifica se o pacote instalado satisfaz a versão mínima dada:

`pacman --deptest "{{bash>=5}}"`

- Verifica se uma versão posterior de um pacote está instalado:

`pacman --deptest "{{bash>5}}"`

- Exibe ajuda:

`pacman --deptest --help`
