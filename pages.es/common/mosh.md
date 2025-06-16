# mosh

> Mobile Shell (`mosh`) es un reemplazo robusto y receptivo para SSH.
> `mosh` persiste las conexiones con servidores remotos mientras deambula en las redes.
> Más información: <https://manned.org/mosh>.

- Conecta a un servidor remoto:

`mosh {{usuario}}@{{equipo_remoto}}`

- Conecta a un servidor remoto con una identidad específica (clave privada):

`mosh --ssh="ssh -i {{ruta/a/archivo_de_clave}}" {{usuario}}@{{equipo_remoto}}`

- Conecta a un servidor remoto usando un puerto específico:

`mosh --ssh="ssh -p {{2222}}" {{usuario}}@{{equipo_remoto}}`

- Ejecuta un comando en un servidor remoto:

`mosh {{equipo_remoto}} -- {{comando -con --opciones}}`

- Selecciona un puerto UDP Mosh (útil cuando el `equipo_remoto` está tras un NAT):

`mosh -p {{124}} {{usuario}}@{{equipo_remoto}}`

- Se lo usa cuando el binario `mosh-server` no se encuentra en la ruta estándar:

`mosh --server={{ruta/a/bin/}}mosh-server {{equipo_remoto}}`
