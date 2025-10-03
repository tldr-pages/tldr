# fgrep

> Compara cadenas fijas en archivos.
> Equivale a `grep -F`.
> Más información: <https://www.gnu.org/software/grep/manual/grep.html>.

- Busca una cadena exacta en un archivo:

`fgrep {{cadena_buscada}} {{ruta/al/archivo}}`

- Busca solo líneas que coincidan totalmente en uno o varios archivos:

`fgrep {{[-x|--line-regexp]}} {{cadena_de_búsqueda}} {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Cuenta el número de líneas que coinciden con la cadena dada en un archivo:

`fgrep {{[-c|--count]}} {{cadena_de_búsqueda}} {{ruta/al/archivo}}`

- Mostrar el número de línea del archivo junto con la línea buscada:

`fgrep {{[-n|--line-number]}} {{cadena_de_búsqueda}} {{ruta/al/archivo}}`

- Muestra todas las líneas excepto las que contienen la cadena de búsqueda:

`fgrep {{[-v|--invert-match]}} {{cadena_de_búsqueda}} {{ruta/al/archivo}}`

- Muestra los nombres de archivo cuyo contenido coincide al menos una vez con la cadena de búsqueda:

`fgrep {{[-l|--files-with-matches]}} {{cadena_de_búsqueda}} {{ruta/al/archivo1 ruta/al/archivo2 ...}}`
