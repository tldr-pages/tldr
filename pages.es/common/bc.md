# bc

> Un lenguaje de calculadora de precisión arbitraria.
> Vea también: `dc`.
> Más información: <https://manned.org/man/bc.1>.

- Inicia una sesión interactiva:

`bc`

- Inicia una sesión interactiva con la biblioteca matemática estándar activada:

`bc --mathlib`

- Calcula una expresión:

`echo '{{5 / 3}}' | bc`

- Ejecuta un script:

`bc {{ruta/al/script.bc}}`

- Calcula una expresión con la escala especificada:

`echo 'scale = {{10}}; {{5 / 3}}' | bc`

- Calcula una función seno/coseno/arctangente/logaritmo natural/exponencial utilizando `mathlib`:

`echo '{{s|c|a|l|e}}({{1}})' | bc --mathlib`
