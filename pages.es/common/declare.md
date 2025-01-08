# declare

> Declara variables y les da atributos.
> Más información: <https://www.gnu.org/software/bash/manual/bash.html#index-declare>.

- Describe una variable de cadena con el valor especificado:

`declare {{variable}}="{{valor}}"`

- Declara una variable entera con el valor especificado:

`declare -i {{variable}}="{{valor}}"`

- Describe una variable arreglo con el valor especificado:

`declare -a {{variable}}=({{item_a item_b item_c}})`

- Declara una variable arreglo asociativo con el valor especificado:

`declare -A {{variable}}=({{[key_a]=item_a [key_b]=item_b [key_c]=item_c}})`

- Declara una variable de cadena de solo lectura con el valor especificado:

`declare -r {{variable}}="{{valor}}"`

- Declara una variable global dentro de una función con el valor especificado:

`declare -g {{variable}}="{{valor}}"`
