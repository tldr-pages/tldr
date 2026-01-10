# apropos

> Busca nombres y descripciones en las páginas del manual.
> Vea también: `man`.
> Más información: <https://manned.org/apropos>.

- Busca una palabra clave utilizando una `regex`:

`apropos {{expresion_regular}}`

- Busca sin restringir la salida al ancho de la terminal:

`apropos {{[-l|--long]}} {{expresion_regular}}`

- Busca páginas que contengan todas las expresiones dadas:

`apropos {{expresion_regular_1}} {{[-a|--and]}} {{expresion_regular_2}} {{[-a|--and]}} {{expresion_regular_3}}`
