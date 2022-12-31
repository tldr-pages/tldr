# ack

> Una herramienta de búsqueda como grep, optimizada para desarrolladores.
> Ver también: `rg`, que es más rápido.
> More information: <https://beyondgrep.com/documentation>.

- Busca archivos que contengan una cadena o expresión regular en el directorio actual de forma recursiva:

`ack "{{patrón_de_búsqueda}}"`

- Buscar de un patrón sin distinción entre mayúsculas y minúsculas:

`ack --ignore-case "{{patrón_de_búsqueda}}"`

- Buscar líneas que coincidan con un patrón, imprimiendo s[o]lamente el texto coincidente y no el resto de la línea:

`ack -o "{{search_pattern}}"`

- Limitar la búsqueda a archivos de un tipo específico:

`ack --type={{ruby}} "{{search_pattern}}"`

- No buscar en archivos dado un tipo específico:

`ack --type=no{{ruby}} "{{search_pattern}}"`

- Contar el número total de coincidencias encontradas:

`ack --count --no-filename "{{search_pattern}}"`

- Imprime sólo los nombres de los ficheros y el número de coincidencias de cada fichero:

`ack --count --files-with-matches "{{search_pattern}}"`

- Lista de todos los valores que se pueden utilizar con `--type`.:

`ack --help-types`
