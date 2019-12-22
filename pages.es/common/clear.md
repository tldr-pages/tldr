# clear

> Limpia la pantalla de la terminal.

- Limpia la pantalla de la terminal (equivale a Control-L cuando se utiliza interfaz de línea de comandos Bash):

`clear`

- Limpia la pantalla pero mantiene el buffer de desplazamiento:

`clear -x`

- Indica el tipo de terminal a limpiar (normalmente esta opción es innecesaria porque se obtiene a partir de la variable de entorno `TERM`):

`clear -T {type_of_terminal}`

- Muestra la versión de `ncurses` utilizada por `clear`:

`clear -V`
