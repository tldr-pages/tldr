# nxc ftp

> Prueba y explota servidores FTP.
> Más información: <https://www.netexec.wiki/ftp-protocol>.

- Busca credenciales válidas probando cada combinación en las listas especificadas de nombres de [u]suario y contraseñas:

`nxc ftp {{192.168.178.2}} -u {{ruta/a/nombres_de_usuario.txt}} -p {{ruta/a/contraseñas.txt}}`

- Continúa buscando credenciales válidas incluso después de haberlas encontrado:

`nxc ftp {{192.168.178.2}} -u {{ruta/a/nombres_de_usuario.txt}} -p {{ruta/a/contraseñas.txt}} --continue-on-success`

- Realiza listados de directorios en cada servidor FTP en el que sean válidas las credenciales proporcionadas:

`nxc ftp {{192.168.178.0/24}} -u {{usuario}} -p {{contraseña}} --ls`

- Descarga el archivo especificado desde el servidor de destino:

`nxc ftp {{192.168.178.2}} -u {{usuario}} -p {{contraseña}} --get {{ruta/al/archivo}}`

- Carga el archivo especificado en el servidor de destino en la ubicación especificada:

`nxc ftp {{192.168.178.2}} -u {{usuario}} -p {{contraseña}} --put {{ruta/al/archivo_local}} {{ruta/a/ubicación_remota}}`
