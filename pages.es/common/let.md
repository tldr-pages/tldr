# let

> Evalúa expresiones aritméticas en el interprete de comandos.
> Más información: <https://www.gnu.org/software/bash/manual/bash.html#index-let>.

- Evalúa una expresión aritmética simple:

`let "{{result = a + b}}"`

- Utiliza el post-incremento y la asignación en una expresión:

`let "{{x++}}"`

- Utiliza el operador condicional en una expresión:

`let "{{result = (x > 10) ? x : 0}}"`

- Muestra la ayuda:

`let --help`
