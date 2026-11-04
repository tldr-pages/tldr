# print

> Comando integrado de Z Shell (`zsh`). Muestra los argumentos, de forma similar a `echo`.
> Vea también: `echo`, `printf`, `zsh`.
> Más información: <https://zsh.sourceforge.io/Doc/Release/Shell-Builtin-Commands.html>.

- Muestra la entrada:

`print "Hello" "World"`

- Imprime separado por saltos de línea:

`print -l "Línea 1" "Línea 2" "Línea 3"`

- Imprime sin salto de línea al final:

`print -n "Hola"; print "Mundo"`

- Habilita caracteres de escape con barra invertida:

`print -e "Línea 1\nLínea 2"`

- Imprime argumentos tal y como se describe en `printf` (para una mayor portabilidad entre intérprete de comandos, considera utilizar el comando `printf` en su lugar):

`print -f "%s tiene %d años.\n" "Alice" 30`
