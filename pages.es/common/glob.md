# glob

> Los patrones glob (`glob`) son patrones que se utilizan para buscar coincidencias en texto.
> Nota: `glob` no es un comando, sino una sintaxis que se utiliza junto con otros comandos o con el shell.
> Vea también: `regex`.
> Más información: <https://en.wikipedia.org/wiki/Glob_(programming)>.

- Busca cero o más caracteres cualesquiera:

`*`

- Busca cualquier carácter individual:

`?`

- Busca un carácter de entre un conjunto de caracteres:

`[{{abc}}]`

- Busca rangos de caracteres:

`[{{a-z}}][{{3-9}}]`

- Coincide con cualquier carácter excepto el especificado:

`[!{{a}}]`

- Coincide con un carácter único que no esté dentro de un rango:

`[!{{a-z}}]`
