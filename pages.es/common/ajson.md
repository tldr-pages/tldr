# ajson

> Ejecuta JSONPath en objetos JSON.
> Más información: <https://github.com/spyzhov/ajson>.

- Lee JSON de un archivo y ejecuta una expresión JSONPath especificada:

`ajson '{{$..json[?(@.path)]}}' {{ruta/a/archivo.json}}`

- Lee JSON de `stdin` y ejecuta una expresión JSONPath especificada:

`cat {{path/to/file.json}} | ajson '{{$..json[?(@.path)]}}'`

- Lee JSON de una URL y evalúa una expresión JSONPath especificada:

`ajson '{{avg($..price)}}' '{{https://ejemplo.com/api/}}'`

- Lee un simple cadena JSON y calcula un valor:

`echo '{{3}}' | ajson '{{2 * pi * $}}'`
