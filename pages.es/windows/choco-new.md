# choco new

> Genera nuevos archivos de especificación de paquetes con Chocolatey.
> Más información: <https://chocolatey.org/docs/commands-new>.

- Crear una nueva estructura de paquete:

`choco new {{paquete}}`

- Crear un nuevo paquete con una versión específica:

`choco new {{paquete}} --version {{versión}}`

- Crear un nuevo paquete con un nombre de mantenedor específico:

`choco new {{paquete}} --maintainer {{nombre_mantenedor}}`

- Crear un nuevo paquete en un directorio de salida personalizado:

`choco new {{paquete}} --output-directory {{ruta/al/directorio}}`

- Crear un nuevo paquete con URLs de instalador específicas para 32 bits y 64 bits:

`choco new {{paquete}} url="{{url}}" url64="{{url}}"`
