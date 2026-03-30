# ssh-keygen

> Genera claves SSH usadas para autenticación, inicios de sesión sin contraseña y otras tareas.
> Vea también: `ssh-copy-id`.
> Más información: <https://man.openbsd.org/ssh-keygen>.

- Genera una clave de forma interactiva:

`ssh-keygen`

- Genera una clave ed25519 con 32 rondas de la función de derivación de claves y guarda la clave en un archivo específico:

`ssh-keygen -t ed25519 -a 32 -f {{~/.ssh/nombre_de_archivo}}`

- Genera una clave RSA de 4096 bits con un correo electrónico como comentario:

`ssh-keygen -t rsa -b 4096 -C "{{comentario|correo_electronico}}"`

- Elimina las claves de un host del archivo `known_hosts` (útil cuando un host conocido tiene una nueva clave):

`ssh-keygen -R {{host_remoto}}`

- Obtiene la huella digital de una clave en MD5 Hex:

`ssh-keygen -l -E md5 -f {{~/.ssh/nombre_de_archivo}}`

- Cambia la contraseña de una clave:

`ssh-keygen -p -f {{~/.ssh/nombre_de_archivo}}`

- Cambia el tipo de formato de la clave (por ejemplo, de formato OPENSSH a PEM), el archivo se reescribirá en el lugar:

`ssh-keygen -p -m PEM -f {{~/.ssh/clave_privada_OpenSSH}}`

- Obtiene la clave pública a partir de la clave privada:

`ssh-keygen -y -f {{~/.ssh/clave_privada_OpenSSH}}`
