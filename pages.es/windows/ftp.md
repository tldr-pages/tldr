# ftp

> Transferir archivos de forma interactiva entre un servidor FTP local y remoto.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/ftp>.

- Conectar a un servidor FTP remoto de forma interactiva:

`ftp {{host}}`

- Iniciar sesión como usuario anónimo:

`ftp -A {{host}}`

- Deshabilitar el inicio de sesión automático al conectarse inicialmente:

`ftp -n {{host}}`

- Ejecutar un archivo que contenga una lista de comandos FTP:

`ftp -s:{{ruta\al\archivo}} {{host}}`

- Descargar múltiples archivos (expresión glob):

`mget {{*.png}}`

- Subir múltiples archivos (expresión glob):

`mput {{*.zip}}`

- Eliminar múltiples archivos en el servidor remoto:

`mdelete {{*.txt}}`

- Mostrar ayuda:

`ftp --help`
