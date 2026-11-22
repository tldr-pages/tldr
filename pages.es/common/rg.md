# rg

> Ripgrep, una herramienta de búsqueda recursiva orientada a líneas.
> Aspira a ser una alternativa más rápida a `grep`.
> Más información: <https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md>.

- Busca de forma recursiva un patrón (`regex`) en el directorio actual:

`rg {{patrón}}`

- Busca de forma recursiva un patrón en un archivo o directorio:

`rg {{patrón}} {{ruta/al/archivo_o_directorio}}`

- Busca un patrón de cadena literal:

`rg {{[-F|--fixed-strings]}} -- {{cadena}}`

- Incluye los archivos ocultos y las entradas listadas en `.gitignore`:

`rg {{[-.|--hidden]}} --no-ignore {{patrón}}`

- Busca solo en los archivos que coinciden con los patrones `glob` (p. ej., `README.*`; use `!patrón_de_nombre_de_archivo` para excluirlos en su lugar):

`rg {{patrón}} {{[-g|--glob]}} '{{patrón_glob_de_nombre_de_archivo}}'`

- Lista de forma recursiva los nombres de archivo del directorio actual y resalta los que coinciden con un patrón:

`rg --files | rg {{[--passthru|--passthrough]}} {{patrón}}`

- Lista solo los archivos con coincidencias (útil al redirigir la salida a otros comandos):

`rg {{[-l|--files-with-matches]}} {{patrón}}`

- Muestra las líneas que no coinciden con el patrón:

`rg {{[-v|--invert-match]}} {{patrón}}`
