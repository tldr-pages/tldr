# return

> Sale de una función o un script si se ejecuta con `source`.
> Más información: <https://www.gnu.org/software/bash/manual/bash.html#index-return>.

- Sale prematuramente de una función:

`{{nombre_de_la_función}}() { {{echo "Se ha alcanzado"}}; return; {{echo "No se ha alcanzado"}}; }`

- Especifica el valor de retorno de la función:

`{{nombre_de_la_función}}() { return {{N}}; }`
