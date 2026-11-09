# read

> Comando integrado del shell para recuperar datos de `stdin`.
> Más información: <https://www.gnu.org/software/bash/manual/bash.html#index-read>.

- Almacena los datos que introduzcas desde el teclado en una o varias variables:

`read {{variable1 variable2 ...}}`

- Almacena cada una de las siguientes líneas que ingreses como valores de un array:

`read -a {{arreglo}}`

- Especifica el número máximo de caracteres que se van a leer:

`read -n {{recuento_de_caracteres}} {{variable}}`

- Asigna varios valores a varias variables:

`read <<<"{{El apellido es Bond}}" {{_ variable1 _ variable2}}`

- Evita que la barra invertida (`\`) actúe como carácter de escape:

`read -r {{variable}}`

- Muestra un mensaje de solicitud antes de la entrada:

`read -p "{{Ingrese aquí tu entrada: }}" {{variable}}`

- No muestra los caracteres tecleados (modo silencioso):

`read -s {{variable}}`

- Realiza una acción en cada línea de la salida de un comando:

`{{comando}} | while IFS= read -r line; do {{echo|ls|rm|...}} "$line"; done`
