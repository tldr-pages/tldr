# declare

> Declara variables y les da atributos.
> Más información: <https://www.gnu.org/software/bash/manual/bash.html#index-declare>.

- Declara una variable de cadena con el valor especificado:

`declare {{variable}}="{{valor}}"`

- Declara una variable entera con el valor especificado:

`declare -i {{variable}}="{{valor}}"`

- Declare una variable de matriz con el valor especificado:

`declare -a {{variable}}=({{artículo_a artículo_b artículo_c}})`

- Declare una variable de matriz asociativa con el valor especificado:

`declare -A {{variable}}=({{[key_a]=item_a [key_b]=item_b [key_c]=item_c}})`

- Declara una variable de cadena de sólo lectura con el valor especificado:

`declare -r {{variable}}="{{valor}}"`

- Declara una variable global dentro de una función con el valor especificado:

`declare -g {{variable}}="{{valor}}"`

- Imprime la definición de una función:

`declare -f {{nombre_función}}`
