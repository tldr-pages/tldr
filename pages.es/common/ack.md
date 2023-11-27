# ack

> Una herramienta de búsqueda como grep, optimizada para desarrolladores.
> Ver también: `rg`, que es más rápido.
> Más información: <https://beyondgrep.com/documentation>.

- Busca archivos que contengan una cadena o expresión regular en el directorio actual de forma recursiva:

`ack "{{patrón_de_búsqueda}}"`

- Busca un patrón sin distinción entre mayúsculas y minúsculas:

`ack --ignore-case "{{patrón_de_búsqueda}}"`

- Busca líneas que coincidan con un patrón, imprimiendo s[o]lamente el texto coincidente y no el resto de la línea:

`ack -o "{{patrón_de_búsqueda}}"`

- Limita la búsqueda a archivos de un tipo específico:

`ack --type={{ruby}} "{{patrón_de_búsqueda}}"`

- No buscar en archivos dado un tipo específico:

`ack --type=no{{ruby}} "{{patrón_de_búsqueda}}"`

- Cuenta el número total de coincidencias encontradas:

`ack --count --no-filename "{{patrón_de_búsqueda}}"`

- Imprime sólo los nombres de los archivos y el número de coincidencias de cada archivo:

`ack --count --files-with-matches "{{patrón_de_búsqueda}}"`

- Lista todos los valores que se pueden utilizar con `--type`:

`ack --help-types`
