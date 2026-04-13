# egrep

> Busca patrones en archivos utilizando expresiones regulares extendidas.
> Nota: Este comando es un alias de `grep --extended-regexp`.
> Más información: <https://manned.org/egrep>.

- Busca uno o más caracteres repetidos:

`egrep '{{a}}+' {{ruta/al/archivo}}`

- Busca cero o una aparición de un carácter (coincidencia opcional):

`egrep '{{a}}?' {{ruta/al/archivo}}`

- Busca 10 repeticiones de un carácter:

`egrep '{{a}}{10}' {{ruta/al/archivo}}`

- Busca entre 3 y 7 repeticiones de un carácter:

`egrep '{{a}}{3,7}' {{ruta/al/archivo}}`

- Busca una de las opciones enumeradas:

`egrep '{{gato}}|{{perro}}|{{ratón}}' {{ruta/al/archivo}}`

- Busca una de las opciones enumeradas dentro de un patrón más amplio:

`egrep 'c({{a}}|{{o}}|{{u}})p' {{ruta/al/archivo}}`

- Busca un grupo de caracteres que se repita una o más veces:

`egrep '({{aeiou}})+' {{ruta/al/archivo}}`

- Busca utilizando clases de caracteres estándar (más información: <https://www.regular-expressions.info/posixbrackets.html>):

`egrep [[{{:alnum:|:alpha:|:space:|...}}]] {{ruta/al/archivo}}`
