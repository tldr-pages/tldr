# dc

> Una calculadora de precisión arbitraria. Utiliza notación polaca inversa (RPN).
> Vea también: `bc`, `qalc`.
> Más información: <https://www.gnu.org/software/bc/manual/dc-1.05/html_mono/dc.html>.

- Inicia una sesión interactiva:

`dc`

- Ejecuta un script:

`dc {{ruta/a/script.dc}}`

- Calcula una expresión con la escala especificada:

`dc {{[-e|--expression]}} '{{10}} k {{5 3 /}} p'`

- Calcula 4 veces 5 (4 5 *), resta 17 (17 -), e im[p]rime la salida:

`dc {{[-e|--expression]}} '4 5 * 17 - p'`

- Especifica el número de decimales a 7 (7 k), calcula 5 dividido por -3 (5 _3 /) y lo im[p]rime:

`dc {{[-e|--expression]}} '7 k 5 _3 / p'`

- Calcula la proporción áurea, phi: establece el número de decimales a 100 (100 k), raíz cuadrada de 5 (5 v) más 1 (1 +), dividido por 2 (2 /), e im[p]rime el resultado:

`dc {{[-e|--expression]}} '100 k 5 v 1 + 2 / p'`
