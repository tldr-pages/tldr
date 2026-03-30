# ssh-copy-id

> Instala tu clave pública en el archivo authorized_keys de una máquina remota.
> Más información: <https://manned.org/ssh-copy-id>.

- Copia tus claves a la máquina remota:

`ssh-copy-id {{usuario}}@{{host_remoto}}`

- Copia la clave pública indicada al equipo remoto:

`ssh-copy-id -i {{ruta/al/certificado}} {{usuario}}@{{host_remoto}}`

- Copia la clave pública indicada al equipo remoto con un puerto específico:

`ssh-copy-id -i {{ruta/al/certificado}} -p {{puerto}} {{usuario}}@{{host_remoto}}`
