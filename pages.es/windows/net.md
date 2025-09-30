# net

> Utilidad del sistema para ver y modificar configuraciones relacionadas con la red.
> Más información: <https://learn.microsoft.com/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/gg651155(v=ws.11)>.

- Inicia o detiene un servicio de Windows de forma sincrónica:

`net {{start|stop}} {{servicio}}`

- Se asegura que un recurso compartido SMB esté disponible en la consola actual:

`net use {{\\carpeta_compartida_smb}} /USER:{{nombre_de_usuario}}`

- Muestra las carpetas actualmente compartidas a través de SMB:

`net share`

- Muestra quién está utilizando tus recursos compartidos SMB (ejecutar en consola elevada):

`net session`

- Muestra usuarios en un grupo de seguridad local:

`net localgroup "{{Administradores}}"`

- Agrega un usuario al grupo de seguridad local (ejecutar en consola elevada):

`net localgroup "{{Administradores}}" {{nombre_de_usuario}} /add`

- Muestra ayuda para un subcomando:

`net help {{subcomando}}`

- Muestra la ayuda:

`net help`
