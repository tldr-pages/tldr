# choco new

> Genera nuevos archivos de especificación de paquetes con Chocolatey.
> Más información: <https://docs.chocolatey.org/en-us/create/commands/new/>.

- Crea una nueva estructura de paquete:

`choco new {{paquete}}`

- Crea un nuevo paquete con una versión específica:

`choco new {{paquete}} --version {{versión}}`

- Crea un nuevo paquete con un nombre de mantenedor específico:

`choco new {{paquete}} --maintainer {{nombre_mantenedor}}`

- Crea un nuevo paquete en un directorio de salida personalizado:

`choco new {{paquete}} {{[--out|--output-directory]}} {{ruta/al/directorio}}`

- Crea un nuevo paquete con URLs de instalador específicas para 32 bits y 64 bits:

`choco new {{paquete}} url="{{url}}" url64="{{url}}"`
