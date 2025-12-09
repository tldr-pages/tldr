# expr

> Evalúa expresiones y manipula cadenas.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/expr-invocation.html>.

- Obtiene la longitud de una cadena específica:

`expr length "{{cadena}}"`

- Obtiene la subcadena de una cadena con una longitud específica:

`expr substr "{{cadena}}" {{desde}} {{longitud}}`

- Empareja una subcadena específica frente a un patrón:

`expr match "{{cadena}}" '{{patrón}}'`

- Obtiene la primera posición de un caracter de un conjunto específico en una cadena:

`expr index "{{cadena}}" "{{caracteres}}"`

- Calcula una expresión matemática específica:

`expr {{expresión1}} {{+|-|*|/|%}} {{expresión2}}`

- Obtiene la primera expresión si su valor no es cero y no nulo, de otro modo, obtiene el segundo:

`expr {{expresión1}} \| {{expresión2}}`

- Obtiene la primera expresión si ambas expresiones no son cero y no nulas de otro modo obtiene cero:

`expr {{expresión1}} \& {{expresión2}}`
