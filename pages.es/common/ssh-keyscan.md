# ssh-keyscan

> Obtiene las claves SSH públicas de hosts remotos.
> Más información: <https://man.openbsd.org/ssh-keyscan>.

- Obtiene todas las claves SSH públicas de un host remoto:

`ssh-keyscan {{nombre_host}}`

- Obtiene todas las claves SSH públicas de un host remoto escuchando en un puerto específico:

`ssh-keyscan -p {{puerto}} {{nombre_host}}`

- Obtiene ciertos tipos de claves SSH públicas de un host remoto:

`ssh-keyscan -t {{rsa,dsa,ecdsa,ed25519}} {{nombre_host}}`

- Actualiza manualmente el archivo SSH known_hosts con la huella digital de un host dado:

`ssh-keyscan -H {{nombre_host}} >> ~/.ssh/known_hosts`
