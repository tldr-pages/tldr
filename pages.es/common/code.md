# code

> Editor de código extensible y multiplataforma.
> Más información: <https://github.com/microsoft/vscode>.

- Inicia Visual Studio Code:

`code`

- Abre archivos o directorios específicos:

`code {{ruta/al/archivo_o_directorio1 ruta/al/archivo_o_directorio2 ...}}`

- Compara dos archivos específicos:

`code --diff {{ruta/al/fichero1}} {{ruta/al/fichero2}}`

- Abre ficheros o directorios específicos en una nueva ventana:

`code --new-window {{ruta/al/fichero_o_directorio1 ruta/al/fichero_o_directorio2 ...}}`

- Instala/desinstala una extensión específica:

`code {{--install-extension | --uninstall-extension}} {{publisher.extension}}`

- Lista las extensiones instaladas:

`code --list-extensions`

- Lista las extensiones instaladas y su versión:

`code --list-extensions --show-versions`

- Ejecuta el editor como súper usuario (root) mientras que almacena los datos del usuario en un directorio específico:

`sudo code --user-data-dir {{ruta/al/directorio}}`
