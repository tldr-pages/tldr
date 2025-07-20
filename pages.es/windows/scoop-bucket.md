# scoop bucket

> Administrar buckets: repositorios Git que contienen archivos que describen cómo scoop instala aplicaciones.
> Si Scoop no sabe dónde se encuentra el bucket, debe especificarse la ubicación del repositorio.
> Más información: <https://github.com/lukesampson/scoop/wiki/Buckets>.

- Listar todos los buckets actualmente en uso:

`scoop bucket list`

- Listar todos los buckets conocidos:

`scoop bucket known`

- Agregar un bucket conocido por su nombre:

`scoop bucket add {{nombre}}`

- Agregar un bucket desconocido por su nombre y URL del repositorio Git:

`scoop bucket add {{nombre}} {{https://example.com/repository.git}}`

- Eliminar un bucket por su nombre:

`scoop bucket rm {{nombre}}`
