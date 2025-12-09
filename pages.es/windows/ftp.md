# ftp

> Transfiere archivos de forma interactiva entre un servidor FTP local y remoto.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/ftp>.

- Conecta a un servidor FTP remoto de forma interactiva:

`ftp {{host}}`

- Inicia sesión como usuario anónimo:

`ftp -A {{host}}`

- Deshabilita el inicio de sesión automático al conectarse inicialmente:

`ftp -n {{host}}`

- Ejecuta un archivo que contenga una lista de comandos FTP:

`ftp -s:{{ruta\al\archivo}} {{host}}`

- Descarga múltiples archivos (expresión glob):

`mget {{*.png}}`

- Sube múltiples archivos (expresión glob):

`mput {{*.zip}}`

- Elimina múltiples archivos en el servidor remoto:

`mdelete {{*.txt}}`

- Muestra la ayuda:

`ftp --help`
