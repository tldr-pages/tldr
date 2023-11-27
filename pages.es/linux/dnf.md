# dnf

> Administrador de paquetes para RHEL, CentOS y Fedora (Reemplaza a yum).
> Más información: <https://dnf.readthedocs.io>.

- Actualiza todos los paquetes a la última versión disponible:

`sudo dnf update`

- Busca un paquete usando palabras clave:

`dnf search {{palabra_clave}}`

- Muestra información acerca de un paquete:

`dnf info {{paquete}}`

- Instala un nuevo paquete:

`sudo dnf install {{paquete}}`

- Instala un nuevo paquete respondiendo sí a todas las preguntas:

`sudo dnf install -y {{paquete}}`

- Lista todos los paquetes instalados:

`dnf list --installed`

- Encuentra qué paquete provee un archivo determinado:

`dnf provides {{archivo}}`
