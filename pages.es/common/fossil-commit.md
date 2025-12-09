# fossil commit

> Envía archivos a un repositorio Fossil.
> Más información: <https://fossil-scm.org/home/help/commit>.

- Crea una nueva versión que contiene todos los cambios en el checkout actual; se solicitará al usuario un comentario:

`fossil commit`

- Crea una versión que contiene todos los cambios en el checkout actual, utilizando el comentario especificado:

`fossil commit --comment "{{comentario}}"`

- Crea una versión que contiene todos los cambios en el checkout actual con un comentario leído de un archivo específico:

`fossil commit --message-file {{ruta/al/archivo_con_comentario}}`

- Crea una versión que contiene cambios de los archivos especificados; se solicitará al usuario un comentario:

`fossil commit {{ruta/al/archivo1 ruta/al/archivo2 ...}}`
