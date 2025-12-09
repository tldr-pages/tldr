# dnf

> Administrador de paquetes para RHEL, CentOS y Fedora (Reemplaza a yum).
> Para comandos equivalentes en otros administradores de paquetes, vea <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> Más información: <https://dnf.readthedocs.io/en/latest/command_ref.html>.

- Actualiza todos los paquetes a la última versión disponible:

`sudo dnf upgrade`

- Busca un paquete usando palabras clave:

`dnf search {{palabra1 palabra2 ...}}`

- Muestra información acerca de un paquete:

`dnf info {{paquete}}`

- Instala un nuevo paquete (usa `-y` para confirmar todas las preguntas automáticamente):

`sudo dnf install {{paquete1 paquete2 ...}}`

- Elimina un paquete:

`sudo dnf remove {{paquete1 paquete2 ...}}`

- Lista todos los paquetes instalados:

`dnf list --installed`

- Encuentra qué paquetes proveen un archivo determinado:

`dnf provides {{archivo}}`

- Ver todas las operaciones pasadas:

`dnf history`
