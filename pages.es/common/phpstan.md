# phpstan

> Una herramienta de análisis estático de PHP para descubrir fallos en el código.
> Más información: <https://phpstan.org/user-guide/command-line-usage>.

- Analiza uno o más directorios:

`phpstan analyse {{ruta/a/directorio1 ruta/a/directorio2 ...}}`

- Analiza un directorio utilizando un archivo de configuración:

`phpstan analyse {{ruta/a/directorio}} {{[-c|--configuration]}} {{ruta/a/configuración}}`

- Analiza usando un nivel de regla específico (0-10, más alto es más estricto):

`phpstan analyse {{ruta/a/directorio}} {{[-l|--level]}} {{nivel}}`

- Especifica un archivo de carga automática para cargar antes de analizar:

`phpstan analyse {{ruta/a/directorio}} {{[-a|--autoload-file]}} {{ruta/archivo/archivo_autocarga}}`

- Especifica un límite de memoria durante el análisis:

`phpstan analyse {{ruta/a/directorio}} --memory-limit {{límite_memoria}}`

- Muestra las opciones disponibles para el análisis:

`phpstan analyse --help`
