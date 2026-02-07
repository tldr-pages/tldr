# compopt

> Imprime o cambia las opciones de completado para un comando.
> `-o` significa habilitado y `+o` significa deshabilitado.
> Vea también: `compgen`, `complete`.
> Más información: <https://www.gnu.org/software/bash/manual/bash.html#index-compopt>.

- Imprime las opciones de finalización para un comando determinado:

`compopt {{comando}}`

- Habilita o deshabilita una opción de finalización de un comando:

`compopt {{-o|+o}} {{opción1}} {{-o|+o}} {{opción2}} {{comando}}`

- Imprime las opciones para la finalización que se está ejecutando actualmente:

`compopt`

- Habilita o deshabilita una opción de finalización de un comando:

`compopt {{-o|+o}} {{opción1}} {{-o|+o}} {{opción2}}`
