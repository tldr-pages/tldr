# trufflehog

> Encuentra y verifica credenciales en archivos, repositorios de Git, cubos S3 e imágenes Docker.
> Más información: <https://github.com/trufflesecurity/trufflehog>.

- Escanea un repositorio de Git en busca de secretos verificados:

`trufflehog git {{https://github.com/trufflesecurity/test_keys}} --only-verified`

- Escanea una organización de GitHub en busca de secretos verificados:

`trufflehog github --org={{trufflesecurity}} --only-verified`

- Escanea un repositorio de GitHub en busca de claves verificadas y genera un archivo de salida JSON:

`trufflehog git {{https://github.com/trufflesecurity/test_keys}} --only-verified --json`

- Escanea un repositorio de GitHub junto con sus incidencias y solicitudes de extracción:

`trufflehog github --repo={{https://github.com/trufflesecurity/test_keys}} --issue-comments --pr-comments`

- Escanea un cubo S3 en busca de claves verificadas:

`trufflehog s3 --bucket={{nombre_del_cubo}} --only-verified`

- Escanea cubos S3 utilizando roles IAM:

`trufflehog s3 --role-arn={{iam-role-arn}}`

- Escanea archivos o directorios individuales:

`trufflehog filesystem {{ruta/al/archivo_o_directorio1 ruta/al/archivo_o_directorio2 ...}}`

- Escanea una imagen de Docker en busca de secretos verificados:

`trufflehog docker --image {{trufflesecurity/secrets}} --only-verified`
