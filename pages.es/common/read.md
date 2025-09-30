# read

> Shell builtin para recuperar datos de `stdin`.
> Más información: <https://www.gnu.org/software/bash/manual/bash.html#index-read>.

- Almacena los datos que escribes desde el teclado:

`read {{variable}}`

- Almacena cada una de las siguientes líneas que introduzcas como valores de un arreglo:

`read -a {{arreglo}}`

- Especifica el número máximo de caracteres a leer:

`read -n {{cuenta_caracteres}} {{variable}}`

- Asigna varios valores a varias variables:

`read {{_ variable1 _ variable2}} <<< "{{El apellido es Bond"}}"`

- No dejes que la barra invertida (\) actúe como carácter de escape:

`read -r {{variable}}`

- Muestra un indicador antes de la entrada:

`read -p "{{Introduce aquí tu entrada: }}" {{variable}}`

- No hacer eco de los caracteres introducidos (modo silencioso):

`read -s {{variable}}`

- Lee `stdin` y realiza una acción en cada línea:

`while read line; do {{echo|ls|rm|...}} "$line"; done < {{dev/stdin|ruta/al/archivo|...}}`
