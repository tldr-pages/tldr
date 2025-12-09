# ack

> Una herramienta de búsqueda como grep, optimizada para desarrolladores.
> Vea también: `rg`, que es más rápido.
> Más información: <https://beyondgrep.com/documentation>.

- Busca archivos que contengan una cadena o expresión regular en el directorio actual de forma recursiva:

`ack "{{patrón_de_búsqueda}}"`

- Busca un patrón sin distinción entre mayúsculas y minúsculas:

`ack {{[-i|--ignore-case]}} "{{patrón_de_búsqueda}}"`

- Busca líneas que coincidan con un patrón, imprimiendo s[o]lamente el texto coincidente y no el resto de la línea:

`ack {{[-o|--output '$&']}} "{{patrón_de_búsqueda}}"`

- Limita la búsqueda a archivos de un tipo específico:

`ack {{[-t|--type]}} {{ruby}} "{{patrón_de_búsqueda}}"`

- Busca archivos que no sean de un cierto tipo:

`ack {{[-t|--type]}} no{{ruby}} "{{patrón_de_búsqueda}}"`

- Cuenta el número total de coincidencias encontradas:

`ack {{[-c|--count]}} {{[-h|--no-filename]}} "{{patrón_de_búsqueda}}"`

- Imprime solo los nombres de los archivos y el número de coincidencias de cada archivo:

`ack {{[-c|--count]}} {{[-l|--files-with-matches]}} "{{patrón_de_búsqueda}}"`

- Lista todos los valores que se pueden utilizar con `--type`:

`ack --help-types`
