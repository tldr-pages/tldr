# tuc

> Corta texto (o bytes) donde coincida un delimitador, luego conserva las partes deseadas.
> Una versión más fácil de usar y potente de `cut` con valores por defecto sensibles.
> Más información: <https://github.com/riquito/tuc>.

- Corta y reorganiza campos:

`echo "foo bar baz" | tuc -d '{{ }}' -f {{3,2,1}}`

- Sustituye el delimitador `space` por una flecha:

`echo "foo bar baz" | tuc -d ' ' -r ' ➡ '`

- Mantiene un rango de campos:

`echo "foo bar baz" | tuc -d ' ' -f {{2:}}`

- Corta usando expresiones regulares:

`echo "a,b, c" | tuc -e '{{[, ]+}}' -f {{1,3}}`

- Genera salida JSON:

`echo "foo bar baz" | tuc -d '{{ }}' --json`
