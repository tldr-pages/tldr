# setarch

> Cambia la arquitectura reportada para la ejecución de un programa, utilizado principalmente para modificar el comportamiento de los programas en función de la arquitectura del sistema.
> Útil para pruebas de compatibilidad o para ejecutar aplicaciones heredadas.
> Más información: <https://manned.org/setarch>.

- Ejecuta un comando como si la arquitectura de la máquina fuera `i686` (útil para ejecutar aplicaciones de 32 bits en un kernel de 64 bits):

`setarch i686 {{comando}}`

- Ejecuta un intérprete de comandos con la arquitectura `x86_64`:

`setarch x86_64 {{bash}}`

- Desactiva la aleatorización del espacio de direcciones virtuales:

`setarch {{linux32}} {{[-R|--addr-no-randomize]}} {{comando}}`

- Enumera las arquitecturas compatibles:

`setarch --list`

- Muestra la ayuda:

`setarch {{[-h|--help]}}`
