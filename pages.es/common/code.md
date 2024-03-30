# code

> Editor de código extensible y multiplataforma.
> Más información: <https://github.com/microsoft/vscode>.

- Inicia Visual Studio Code:

`code`

- Abre archivos o directorios específicos:

`code {{ruta/al/archivo_o_directorio1 ruta/al/archivo_o_directorio2 ...}}`

- Compara dos archivos específicos:

`code --diff {{ruta/al/archivo1}} {{ruta/al/archivo2}}`

- Abre archivos o directorios específicos en una nueva ventana:

`code --new-window {{ruta/al/archivo_o_directorio1 ruta/al/archivo_o_directorio2 ...}}`

- Instala/desinstala una extensión específica:

`code --{{install|uninstall}}-extension {{editor.extension}}`

- Imprime las extensiones instaladas:

`code --list-extensions`

- Imprime las extensiones instaladas con su versión:

`code --list-extensions --show-versions`

- Inicia el editor como súper usuario (root) mientras que almacena los datos del usuario en un directorio específico:

`sudo code --user-data-dir {{ruta/al/directorio}}`
