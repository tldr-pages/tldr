# regex

> Las expresiones regulares (`regex`) son patrones que se utilizan para buscar coincidencias, buscar y manipular texto.
> Nota: `regex` no es un comando, sino una sintaxis que se utiliza con otros comandos.
> Más información: <https://cheatography.com/davechild/cheat-sheets/regular-expressions/>.

- Coincide con cualquier carácter único:

`.`

- Coincide con el inicio de una línea:

`^{{hola}}`

- Coincide con el final de una línea:

`{{mundo}}$`

- Coincide con cero o más caracteres repetidos:

`{{a}}*`

- Coincide con un conjunto de caracteres:

`[{{abc}}]`

- Coincide con rangos de caracteres:

`[{{a-z}}][{{3-9}}]`

- Coincide con cualquier cosa excepto el carácter especificado:

`[^{{a}}]`

- Coincide con un límite alrededor de una palabra:

`"\b{{texto}}\b"`
