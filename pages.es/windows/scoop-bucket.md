# scoop bucket

> Administra buckets: repositorios Git que contienen archivos que describen cómo scoop instala aplicaciones.
> Si Scoop no sabe dónde se encuentra el bucket, debe especificarse la ubicación del repositorio.
> Más información: <https://github.com/ScoopInstaller/Scoop/wiki/Buckets>.

- Lista todos los buckets actualmente en uso:

`scoop bucket list`

- Lista todos los buckets conocidos:

`scoop bucket known`

- Agregar un bucket conocido por su nombre:

`scoop bucket add {{nombre}}`

- Agregar un bucket desconocido por su nombre y URL del repositorio Git:

`scoop bucket add {{nombre}} {{https://example.com/repository.git}}`

- Elimina un bucket por su nombre:

`scoop bucket rm {{nombre}}`
