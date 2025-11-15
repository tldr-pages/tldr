# aws s3 cp

> Copia archivos locales u objetos de S3 a otra ubicación, ya sea local o en S3.
> Más información: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/cp.html>.

- Copia un archivo local a un bucket específico:

`aws s3 cp {{ruta/al/archivo}} s3://{{nombre_bucket}}/{{ruta/al/archivo_remoto}}`

- Copia un objeto específico de S3 a otro bucket:

`aws s3 cp s3://{{nombre_bucket1}}/{{ruta/al/archivo}} s3://{{nombre_bucket2}}/{{ruta/de/destino}}`

- Copia un objeto específico de S3 a otro bucket manteniendo el nombre original:

`aws s3 cp s3://{{nombre_bucket1}}/{{ruta/al/archivo}} s3://{{nombre_bucket2}}`

- Copia objetos de S3 a un directorio local de forma recursiva:

`aws s3 cp s3://{{nombre_bucket}} . --recursive`

- Muestra la ayuda:

`aws s3 cp help`
