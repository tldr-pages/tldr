# bc

> Un lenguaje de calculadora de precisión arbitraria.
> Vea también: `dc`, `qalc`.
> Más información: <https://manned.org/bc>.

- Inicia una sesión interactiva:

`bc`

- Inicia una sesión [i]nteractiva con la bib[l]ioteca matemática estándar activada:

`bc --interactive --mathlib`

- Calcula una expresión:

`echo '{{5 / 3}}' | bc`

- Ejecuta un script:

`bc {{ruta/al/script.bc}}`

- Calcula una expresión con la escala especificada:

`echo 'scale = {{10}}; {{5 / 3}}' | bc`

- Calcula una función seno/coseno/arctangente/logaritmo natural/exponencial utilizando `mathlib`:

`echo '{{s|c|a|l|e}}({{1}})' | bc --mathlib`

- Ejecuta un guión factorial en línea (inline):

`echo "define factorial(n) { if (n <= 1) return 1; return n*factorial(n-1); }; factorial({{10}})" | bc`
