# egrep

> Busca patrones en archivos utilizando expresiones regulares extendidas.
> Nota: Este comando es un alias de `grep --extended-regexp`.
> Más información: <https://manned.org/egrep>.

- Busca uno o más caracteres repetidos:

`egrep “{{a}}+” {{ruta/al/archivo}}`

- Busca entre cero o una aparición de un carácter (coincidencia opcional):

`egrep “{{a}}?” {{ruta/al/archivo}}`

- Busca 10 repeticiones de un carácter:

`egrep “{{a}}{10}” {{ruta/al/archivo}}`

- Busca una de las opciones de la lista:

`egrep “({{gato}}|{{perro}}|{{ratón})” {{ruta/al/archivo}}`

- Busca utilizando clases de caracteres estándar (más información: <https://www.regular-expressions.info/posixbrackets.html>):

`egrep [[{{:alnum:|:alpha:|:space:|...}}]] {{ruta/al/archivo}}`
