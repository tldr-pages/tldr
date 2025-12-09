# mc

> Cliente MinIO para almacenamiento de objetos y sistemas de archivos.
> Puede llamarse `mc` o `mcli` en algunos sistemas.
> Más información: <https://minio.github.io/mc/>.

- Añade conexión a un servidor S3:

`mc alias set {{local}} {{http://localhost:9000}} {{clave_acceso}} {{clave_secreta}}`

- Crea un bucket:

`mc mb {{local/nombre_cubo}}`

- Lista cubos y su contenido de forma recursiva:

`mc ls {{local}} --recursive`
