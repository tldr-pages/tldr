# bc

> Un lenguaje de calculadora de precisión arbitraria.
> Vea también: `dc`.
> Más información: <https://keith.github.io/xcode-man-pages/bc.1.html>.

- Inicia una sesión interactiva:

`bc`

- Inicia una sesión interactiva con la biblioteca mathlib estándar activada:

`bc --mathlib`

- Calcula una expresión:

`bc --expression='{{5 / 3}}'`

- Ejecuta un script:

`bc {{ruta/al/script.bc}}`

- Calcula una expresión con la escala especificada:

`bc --expression='scale = {{10}}; {{5 / 3}}'`

- Calcula una función seno/coseno/arctangente/logaritmo natural/exponencial utilizando `mathlib`:

`bc --mathlib --expression='{{s|c|a|l|e}}({{1}})'`
