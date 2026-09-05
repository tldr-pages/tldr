# secon

> Obtiene el contexto de seguridad de SELinux de un archivo, un PID, el contexto de ejecución actual o una especificación de contexto.
> Vea también: `semanage`, `runcon`, `chcon`.
> Más información: <https://manned.org/secon>.

- Obtiene el contexto de seguridad del contexto de ejecución actual:

`secon`

- Obtiene el contexto de seguridad actual de un proceso:

`secon --pid {{1}}`

- Obtiene el contexto de seguridad actual de un archivo, resolviendo todos los enlaces simbólicos intermedios:

`secon --file {{ruta/al/archivo_o_directorio}}`

- Obtiene el contexto de seguridad actual del propio enlace simbólico (es decir, sin resolverlo):

`secon --link {{ruta/al/enlace_simbólico}}`

- Analiza y explica una especificación de contexto:

`secon {{system_u:system_r:container_t:s0:c899,c900}}`
