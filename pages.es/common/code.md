# code

> Editor de código extensible y multiplataforma.
> Más información: <https://github.com/microsoft/vscode>.

- Ejecuta Visual Studio Code:

`code`

- Abre ficheros o directorios específicos:

`code {{ruta/al/fichero_o_directorio1 ruta/al/fichero_o_directorio2 ...}}`

- Compara dos ficheros específicos:

`code --diff {{ruta/al/fichero1}} {{ruta/al/fichero2}}`

- Abre ficheros o directorios específicos en una nueva ventana:

`code --new-window {{ruta/al/fichero_o_directorio1 ruta/al/fichero_o_directorio2 ...}}`

- Instala una extensión específica:

`code --install-extension {{publisher.extension}}`

- Desinstala una extensión específica:

`code --uninstall-extension {{publisher.extension}}`

- Lista las extensiones instaladas:

`code --list-extensions`

- Lista las extensiones instaladas y su versión:

`code --list-extensions --show-versions`

- Ejecuta el editor como súper usuario (root) mientras que almacena los datos del usuario en un directorio específico:

`sudo code --user-data-dir {{ruta/al/directorio}}`
