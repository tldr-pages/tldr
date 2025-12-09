# valgrind

> Programa para un conjunto de herramientas expertas con programas de perfilado, optimización y depuración.
> Entre las herramientas de uso común cabe citar: `memcheck`, `cachegrind`, `callgrind`, `massif`, `helgrind` y `drd`.
> Más información: <https://valgrind.org/docs/manual/manual-core.html#manual-core.options>.

- Utiliza la herramienta Memcheck (por defecto) para mostrar un diagnóstico del uso de la memoria por `programa`:

`valgrind {{programa}}`

- Utiliza Memcheck para informar sobre todas las posibles fugas de memoria de `programa` en detalle:

`valgrind --leak-check=full --show-leak-kinds=all {{programa}}`

- Utiliza la herramienta Cachegrind para perfilar y registrar operaciones de caché de CPU de `programa`:

`valgrind --tool=cachegrind {{programa}}`

- Utiliza la herramienta Massif para perfilar y registrar la memoria heap y el uso de la pila de `programa`:

`valgrind --tool=massif --stacks=yes {{programa}}`
