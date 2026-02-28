# bunx

> Ejecuta el binario de un paquete (instalado localmente u obtenido remotamente).
> Nota: `bun x` puede utilizarse como alias de `bunx`.
> Más información: <https://bun.com/docs/pm/bunx>.

- Descarga y ejecuta un paquete desde el registro:

`bunx {{nombre_paquete}} "{{argumento_del_comando}}"`

- Comprueba la versión de un paquete instalado localmente (si se encuentra):

`bunx {{nombre_paquete}} --version`

- Fuerza la ejecución de un ejecutable con el runtime de Bun (en lugar de Node):

`bunx --bun {{nombre_paquete}}

- Ejecuta un binario que tenga un nombre distinto al de su paquete:

`bunx {{[-p|--package]}} {{nombre_paquete}} {{comando}}`

- Descarga y ejecuta una versión específica de un paquete:

`bunx {{nombre_paquete@versión}} "{{argumento_del_comando}}"`
