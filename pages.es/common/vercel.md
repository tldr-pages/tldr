# vercel

> Implementa y gestiona sus implementaciones de Vercel.
> Más información: <https://vercel.com/docs/cli>.

- Implementa el directorio actual:

`vercel`

- Implementa el directorio actual en producción:

`vercel --prod`

- Implementa un directorio:

`vercel {{ruta/al/proyecto}}`

- Inicializa un proyecto de ejemplo:

`vercel init`

- Implementa con variables de entorno:

`vercel {{[-e|--env]}} {{ENV}}={{var}}`

- Compila con variables de entorno:

`vercel {{[-b|--build-env]}} {{ENV}}={{var}}`

- Establece regiones predeterminadas para habilitar la implementación en:

`vercel --regions {{región_id}}`

- Elimina una implementación:

`vercel remove {{nombre_del_proyecto}}`
