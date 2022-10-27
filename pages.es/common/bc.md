# bc

> Un lenguaje de calculadora de precisión arbitraria.
> Más información: <https://manned.org/man/bc.1>.

- Inicia `bc` en el modo interactivo utilizando la biblioteca matemática estándar:

`bc -l`

- Calcula el resultado de una expresión:

`bc <<< "(1 + 2) * 2 ^ 2"`

- Calcula el resultado de una expresión y fuerza a que el resultado tenga 10 cifras decimales:

`bc <<< "scale=10; 5 / 3"`

- Calcula el resultado de una expresión con el seno y coseno utilizando `mathlib`:

`bc -l <<< "s(1) + c(1)"`
