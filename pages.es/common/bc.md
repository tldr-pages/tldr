# bc

> Un lenguaje de calculadora de precisión arbitraria.
> Más información: <https://manned.org/bc>.

- Iniciar `bc` en el modo interactivo utilizando la biblioteca matemática estándar:

`bc -l`

- Calcular el resultado de una expresión:

`bc <<< "(1 + 2) * 2 ^ 2"`

- Calcular el resultado de una expresión y forzar a que el resultado tenga 10 cifras decimales:

`bc <<< "scale=10; 5 / 3"`

- Calcular el resultado de una expresión con el seno y coseno utilizando `mathlib`:

`bc -l <<< "s(1) + c(1)"`
